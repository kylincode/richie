# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("large_banner", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="largebanner",
            name="logo_alt_text",
            field=models.CharField(default="Default value", max_length=255),
            preserve_default=False,
        )
    ]
