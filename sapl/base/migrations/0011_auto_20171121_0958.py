# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-21 11:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_appconfig_painel_aberto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appconfig',
            options={'ordering': ('-id',), 'permissions': (('menu_sistemas', 'Renderizar Menu Sistemas'), ('view_tabelas_auxiliares', 'Visualizar Tabelas Auxiliares')), 'verbose_name': 'Configurações da Aplicação', 'verbose_name_plural': 'Configurações da Aplicação'},
        ),
    ]