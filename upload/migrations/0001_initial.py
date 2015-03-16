# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insertData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_release_date', models.DateTimeField()),
                ('state', models.CharField(max_length=100)),
                ('zone', models.CharField(max_length=100)),
                ('case', models.IntegerField(default=0)),
                ('days_accumulated', models.IntegerField(default=0)),
                ('date_published', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
