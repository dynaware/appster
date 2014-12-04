# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_store', '0010_application_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignrepo',
            name='logo',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foreignrepo',
            name='app_url',
            field=models.URLField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='foreignrepo',
            name='url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
