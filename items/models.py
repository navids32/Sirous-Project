from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=512, null=False, blank=False)


class AnyItem(models.Model):
    serial_number = models.CharField(max_length=100, null=False, blank=False)
    model_item = models.ForeignKey('ModelItem', on_delete=models.SET_NULL, null=True)
    brand_item = models.ForeignKey('BrandItem', on_delete=models.SET_NULL, null=True)
    status_item = models.ForeignKey('StatusItem', on_delete=models.SET_NULL, null=True)
    price_ir = models.IntegerField(null=False, blank=False)
    price_usd = models.IntegerField(null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    date_in = models.DateTimeField(default=datetime.now, blank=False)


class ModelItem(models.Model):
    model_item = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.model_item


class BrandItem(models.Model):
    brand_item = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.brand_item


class StatusItem(models.Model):
    status_item = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.status_item


