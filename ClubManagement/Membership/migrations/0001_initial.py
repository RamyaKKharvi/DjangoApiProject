# Generated by Django 4.2.3 on 2023-10-17 11:58

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(10, message='Age must be greater than 12 years'), django.core.validators.MaxValueValidator(90, message='Age must be less than 90 years')])),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('place', models.CharField(max_length=100)),
                ('subscriber_type', models.IntegerField(choices=[(1, 'Monthly'), (2, 'Semi Annual'), (3, 'Annual')], default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('subscription_date', models.DateField(default=datetime.date.today)),
                ('subscription_renewal_date', models.DateField()),
                ('membership_start_date', models.DateField(default=datetime.date.today)),
                ('membership_end_date', models.DateField(default=None)),
            ],
        ),
    ]
