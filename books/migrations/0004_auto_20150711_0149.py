# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20150711_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='lastChangeDate',
            new_name='last_change_date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='lastChangeDate',
            new_name='last_change_date',
        ),
        migrations.RenameField(
            model_name='publisher',
            old_name='lastChangeDate',
            new_name='last_change_date',
        ),
    ]
