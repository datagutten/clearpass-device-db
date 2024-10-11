from django.db import models
from macaddress.fields import MACAddressField
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    role = models.CharField(max_length=50, unique=True, primary_key=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.role, self.description)


class Device(models.Model):
    mac = MACAddressField(_('MAC-adresse'), unique=True, integer=False)
    description = models.CharField(_('Beskrivelse'), max_length=255)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name=_('Rolle'))
    added_by = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name=_('Lagt til av'))
    added = models.DateTimeField(_('Lagt til'), auto_now_add=True)
    modified = models.DateTimeField(_('Endret'), auto_now=True)
    expiry = models.DateTimeField(_('Utløpsdato'), null=True, blank=True)
    enabled = models.BooleanField(_('Aktivert'), default=True)

    def __str__(self):
        return self.mac

    def is_random(self):
        return str(self.mac)[1] in ['2', '6', 'a', 'e']
