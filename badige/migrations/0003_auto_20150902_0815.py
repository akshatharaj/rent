# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badige', '0002_auto_20150902_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestcard',
            name='marketing_source',
            field=models.ForeignKey(blank=True, to='badige.MarketingSource', null=True),
        ),
    ]
