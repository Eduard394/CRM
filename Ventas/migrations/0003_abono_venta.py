# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0002_venta_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='abono',
            name='venta',
            field=models.ForeignKey(default='20180906', to='Ventas.Venta'),
            preserve_default=False,
        ),
    ]
