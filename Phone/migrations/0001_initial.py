# Generated by Django 3.0.8 on 2022-03-19 06:49

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('itemList', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('keywordsSearch', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
            ],
        ),
    ]
