# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badige', '0004_guestcard_closing_quarter'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestcard',
            name='first_seen_quarter',
            field=models.IntegerField(null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
    ]
