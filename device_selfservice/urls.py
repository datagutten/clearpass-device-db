from django.urls import path

from device_selfservice import views

urlpatterns = [
    path('', views.index, name='index'),
    path('device', views.device_form, name='device_add'),
    path('device/<str:mac>', views.device_form, name='device_change'),
    path('device_list', views.device_list, name='device_list'),
    path('device_list_all', views.device_list_all, name='device_list_all'),
]
