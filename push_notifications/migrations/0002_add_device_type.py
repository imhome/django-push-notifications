# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='APNSDevice',
            name='device_type',
            field=models.CharField(default='UNSET', max_length=5, verbose_name='Device Type', choices=[(b'DEBUG', b'Debug'), (b'BETA', b'Beta'), (b'PROD', b'Prod')]),
            preserve_default=False,
        ),
    ]
