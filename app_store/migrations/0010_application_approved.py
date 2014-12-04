# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0009_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
