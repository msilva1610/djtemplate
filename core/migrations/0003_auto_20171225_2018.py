# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-25 22:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171225_2014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name'], 'verbose_name': 'Grupo', 'verbose_name_plural': 'Grupos'},
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'ordering': ['group'], 'verbose_name': 'Membro', 'verbose_name_plural': 'Membros'},
        ),
    ]
