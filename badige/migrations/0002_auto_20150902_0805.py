# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badige', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestcard',
            name='marketing_source',
            field=models.ForeignKey(to='badige.MarketingSource', null=True),
        ),
    ]
