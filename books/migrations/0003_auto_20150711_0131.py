# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20150710_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='lastChangeDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 1, 31, 36, 124162, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='lastChangeDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 1, 31, 41, 940433, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publisher',
            name='lastChangeDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 1, 31, 47, 732206, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
