import os
from django.db import models
from core.models import User


NULLABLE = {"null": True, "blank": True}


class TgUser(models.Model):
    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, **NULLABLE, default=None)
    user = models.ForeignKey(User, models.PROTECT, **NULLABLE, default=None)
    verification_code = models.CharField(max_length=32)

    def set_verification_code(self):
        code = os.urandom(12).hex()
        self.verification_code = code

    class Meta:
        verbose_name = "tg пользователь"
        verbose_name_plural = "tg пользователи"
