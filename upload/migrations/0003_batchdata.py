# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_document_invite'),
    ]

    operations = [
        migrations.CreateModel(
            name='batchData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=100)),
                ('zone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('cases', models.IntegerField()),
                ('days_accumulated', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
