# Generated by Django 4.0.3 on 2022-12-10 07:31

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plans',
            fields=[
                ('plan_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Netowrk_operator', models.CharField(max_length=30, unique=True)),
                ('locality', models.CharField(blank=True, choices=[('Delhi', 'DELHI'), ('Delhi_ncr', 'DELHI NCR'), ('Mumbai', 'MUMBAI'), ('Kolkata', 'Kolkata'), ('Banglore', 'Banglore')], default='', max_length=100)),
                ('price', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(10)])),
                ('validity', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(365), django.core.validators.MinValueValidator(1)])),
                ('plan_creating_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]