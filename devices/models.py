from django.db import models
from macaddress.fields import MACAddressField


class Role(models.Model):
    role = models.CharField(max_length=50, unique=True, primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.role


class Device(models.Model):
    mac = MACAddressField(unique=True, integer=False)
    description = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    added_by = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    expiry = models.DateTimeField(null=True, blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.mac
