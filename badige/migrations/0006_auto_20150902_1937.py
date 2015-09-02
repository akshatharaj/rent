# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badige', '0005_guestcard_first_seen_quarter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestcard',
            name='closing_quarter',
            field=models.CharField(max_length=7, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='guestcard',
            name='first_seen_quarter',
            field=models.CharField(max_length=7, null=True, blank=True),
        ),
    ]
