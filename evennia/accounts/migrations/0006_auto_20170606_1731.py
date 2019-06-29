# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 17:31


import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160905_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdb',
            name='db_attributes',
            field=models.ManyToManyField(help_text='attributes on this object. An attribute can hold any pickle-able python object (see docs for special cases).', to='typeclasses.Attribute'),
        ),
        migrations.AlterField(
            model_name='accountdb',
            name='db_tags',
            field=models.ManyToManyField(help_text='tags on this object. Tags are simple string markers to identify, group and alias objects.', to='typeclasses.Tag'),
        ),
        migrations.AlterField(
            model_name='accountdb',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
    ]
