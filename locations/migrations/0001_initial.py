# Generated by Django 2.0.7 on 2019-09-05 20:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=2)),
                ('industry', models.CharField(max_length=250)),
                ('subIndustry', models.CharField(max_length=250)),
                ('franchise', models.BooleanField()),
                ('county', models.CharField(max_length=250)),
                ('zipcode', models.CharField(max_length=5)),
                ('newCoDate', models.DateField(null=True)),
                ('sqft', models.FloatField(blank=True, null=True)),
                ('employees', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=3)),
                ('openHours', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=7)),
                ('sfAccountId', models.CharField(max_length=250)),
            ],
        ),
    ]
