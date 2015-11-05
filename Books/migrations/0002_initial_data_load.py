# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import migrations, models
from django.core.management import call_command


def load_fixture(apps, schemaeditor):
    call_command('loaddata', 'initial_data.json')


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_auto_20151105_1322')
    ]

    operations = [
        migrations.RunPython(load_fixture)
    ]
