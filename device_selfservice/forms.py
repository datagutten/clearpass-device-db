from django import forms

from devices.models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ['added_by', 'added', 'modified']

