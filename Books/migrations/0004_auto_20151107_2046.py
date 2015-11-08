# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_auto_20151105_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratingvote',
            old_name='value',
            new_name='vote_value',
        ),
    ]
