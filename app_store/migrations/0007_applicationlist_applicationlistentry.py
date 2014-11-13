# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0006_application_click_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationListEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('application', models.ForeignKey(to='app_store.Application')),
                ('list', models.ForeignKey(to='app_store.ApplicationList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
