from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='item_image')
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey('UserProfile', on_delete=models.PROTECT)


class Auction(models.Model):
    start_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    end_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    item = models.OneToOneField(Item, on_delete=models.PROTECT)


class Bid(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    bid_datetime = models.DateTimeField('%d/%m/%Y %H:%M:%S')
    auction = models.OneToOneField(Auction, on_delete=models.PROTECT)
    user = models.OneToOneField('UserProfile', on_delete=models.PROTECT)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    mobile_regex = RegexValidator(regex=r'^\+44\d{10}$', message='Mobile number must be a valid 12 digit UK number.')
    mobile = models.CharField(validators=[mobile_regex], max_length=12)


