# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badige', '0003_auto_20150902_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestcard',
            name='closing_quarter',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], blank=True, null=True),
        ),
    ]
