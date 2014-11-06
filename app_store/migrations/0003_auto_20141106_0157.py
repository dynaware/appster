# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0002_auto_20141029_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('rating', models.SmallIntegerField()),
                ('review_text', models.TextField(null=True)),
                ('application', models.ForeignKey(to='app_store.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='application',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
