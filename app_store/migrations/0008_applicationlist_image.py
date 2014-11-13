# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0007_applicationlist_applicationlistentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationlist',
            name='image',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
