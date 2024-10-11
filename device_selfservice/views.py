from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from devices import models
from device_selfservice import forms


def index(request):
    return render(request, 'device_selfservice/index.html')


def device_form(request, mac=None):
    if mac:
        device_obj = get_object_or_404(models.Device, mac=mac)
    else:
        device_obj = None
    form = forms.DeviceForm(request.POST or None, instance=device_obj)
    if form.is_valid():
        device_obj = form.save(commit=False)
        if not device_obj.id:
            device_obj.added_by = request.user
        device_obj.save()
        return redirect('device_list')

    return render(request, 'device_selfservice/device_form.html', {'form': form})


@permission_required("devices.change_device", login_url="/loginpage/")
def device_list(request):
    devices = models.Device.objects.filter(added_by=request.user.id)
    return render(request, 'device_selfservice/device_list.html', {'devices': devices})
