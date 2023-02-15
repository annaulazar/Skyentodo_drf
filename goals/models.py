from django.db import models
from django.utils import timezone

from core.models import User


NULLABLE = {"null": True, "blank": True}

class DatesModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name="Создано")
    updated = models.DateTimeField(verbose_name="Обновлено")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class Board(DatesModelMixin):
    class Meta:
        verbose_name = "Доска"
        verbose_name_plural = "Доски"

    title = models.CharField(max_length=255, verbose_name="Наименование")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалена")

    def __str__(self):
        return self.title


class BoardParticipant(DatesModelMixin):
    class Meta:
        unique_together = ("board", "user")
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    class Role(models.IntegerChoices):
        owner = 1, "Владелец"
        writer = 2, "Редактор"
        reader = 3, "Читатель"

    editable_choices = Role.choices
    editable_choices.pop(0)

    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name="boardparticipants", verbose_name="Доска")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="boardparticipants", verbose_name="Пользователь")
    role = models.PositiveSmallIntegerField(choices=Role.choices, default=Role.owner, verbose_name="Роль")


class GoalCategory(DatesModelMixin):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name="categories", verbose_name="Доска")
    title = models.CharField(max_length=255, verbose_name="Наименование")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор")
    is_deleted = models.BooleanField(default=False, verbose_name="Удалена")


class Goal(DatesModelMixin):
    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

    class Status(models.IntegerChoices):
        to_do = 1, "К выполнению"
        in_progress = 2, "В процессе"
        done = 3, "Выполнено"
        archived = 4, "Архив"

    class Priority(models.IntegerChoices):
        low = 1, "Низкий"
        medium = 2, "Средний"
        high = 3, "Высокий"
        critical = 4, "Критический"

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="goals", verbose_name="Пользователь")
    category = models.ForeignKey(GoalCategory, on_delete=models.PROTECT, verbose_name="Категория")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(**NULLABLE, verbose_name="Описание")
    due_date = models.DateField(**NULLABLE, verbose_name="Дата выполнения")
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.to_do, verbose_name="Статус")
    priority = models.PositiveSmallIntegerField(choices=Priority.choices, default=Priority.medium, verbose_name="Приоритет")

    def __str__(self):
        return self.title


class GoalComment(DatesModelMixin):
    class Meta:
        verbose_name = "Комментарий к цели"
        verbose_name_plural = "Комментарии к целям"

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="goal_comments", verbose_name="Автор")
    goal = models.ForeignKey(Goal, on_delete=models.PROTECT, related_name="goal_comments", verbose_name="Цель")
    text = models.TextField(verbose_name="Текст")
