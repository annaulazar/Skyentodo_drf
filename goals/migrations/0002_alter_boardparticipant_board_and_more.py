# Generated by Django 4.1.5 on 2023-02-15 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardparticipant',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='boardparticipants', to='goals.board', verbose_name='Доска'),
        ),
        migrations.AlterField(
            model_name='boardparticipant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='boardparticipants', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]