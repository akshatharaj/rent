# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestCard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('gc_id', models.IntegerField(null=True, blank=True)),
                ('first_seen', models.DateField()),
                ('expected_move_in', models.DateField(null=True, blank=True)),
                ('shown_unit', models.DateField(null=True, blank=True)),
                ('agent_id', models.IntegerField()),
                ('application_submitted', models.DateField(null=True, blank=True)),
                ('application_approved', models.DateField(null=True, blank=True)),
                ('application_cancelled', models.DateField(null=True, blank=True)),
                ('application_denied', models.DateField(null=True, blank=True)),
                ('lease_signed', models.DateField(null=True, blank=True, db_index=True)),
                ('resident_rent', models.DecimalField(decimal_places=2, null=True, max_digits=7, blank=True)),
                ('unit_name', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'get_latest_by': 'lease_signed',
            },
        ),
        migrations.CreateModel(
            name='MarketingSource',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='guestcard',
            name='marketing_source',
            field=models.ForeignKey(to='badige.MarketingSource'),
        ),
    ]
