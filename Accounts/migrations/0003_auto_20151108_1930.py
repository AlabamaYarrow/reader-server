# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0005_auto_20151108_1930'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0002_readeruser_completedbooks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readeruser',
            name='CompletedBooks',
        ),
        migrations.AddField(
            model_name='readeruser',
            name='completed_books',
            field=models.ManyToManyField(to='Books.Book', related_name='completed_books'),
        ),
        migrations.AddField(
            model_name='readeruser',
            name='planned_books',
            field=models.ManyToManyField(to='Books.Book', related_name='planned_books'),
        ),
        migrations.AddField(
            model_name='readeruser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None),
            preserve_default=False,
        ),
    ]
