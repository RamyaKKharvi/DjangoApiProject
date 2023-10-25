from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from datetime import date


class SubscriberChoices(models.IntegerChoices):
    monthly = 1
    semi_annual = 2
    annual = 3


class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(10, message='Age must be greater than 12 years'), MaxValueValidator(90, message='Age must be less than 90 years')])
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    place = models.CharField(max_length=100)
    subscriber_type = models.IntegerField(choices=SubscriberChoices.choices, default=SubscriberChoices.monthly)
    is_active = models.BooleanField(default=True)
    subscription_date = models.DateField(default=date.today)
    subscription_renewal_date = models.DateField()
    membership_start_date = models.DateField(default=date.today)
    membership_end_date = models.DateField(default=None)
