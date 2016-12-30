# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=2048)),
                ('type', models.IntegerField(default=1)),
                ('is_valid', models.BooleanField(default=True)),
                ('create_time', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
