# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0005_auto_20141109_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='click_count',
            field=models.IntegerField(editable=False, default=0),
            preserve_default=True,
        ),
    ]
