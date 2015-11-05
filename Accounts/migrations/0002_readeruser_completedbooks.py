# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Books', '0001_auto_20151105_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='readeruser',
            name='CompletedBooks',
            field=models.ManyToManyField(to='Books.Book'),
        ),
    ]
