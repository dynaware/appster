# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0004_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='logo',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='screenshot',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
