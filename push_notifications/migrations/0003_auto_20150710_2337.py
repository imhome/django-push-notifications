# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0002_add_device_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apnsdevice',
            options={'verbose_name': 'APNS Device'},
        ),
        migrations.AlterModelOptions(
            name='gcmdevice',
            options={'verbose_name': 'GCM Device'},
        ),
    ]
