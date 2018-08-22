# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.IntegerField(null=True, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cartera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saldo', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50, null=True, blank=True)),
                ('cedula', models.CharField(max_length=15, null=True, blank=True)),
                ('apellidos', models.CharField(max_length=50, null=True, blank=True)),
                ('activo', models.BooleanField()),
                ('fecha_crea', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=50, null=True, blank=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('precio_unitario', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_unitario', models.IntegerField(null=True, blank=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('precio_total', models.IntegerField(null=True, blank=True)),
                ('estado_pago', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(to='Ventas.Cliente')),
                ('producto', models.ForeignKey(to='Ventas.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='cartera',
            name='cliente',
            field=models.ForeignKey(to='Ventas.Cliente'),
        ),
        migrations.AddField(
            model_name='abono',
            name='cliente',
            field=models.ForeignKey(to='Ventas.Cliente'),
        ),
    ]
