from django.urls import path

from network.views import ping_page,camera

app_name = "network"

urlpatterns = [
    path("",ping_page, name="ping"),
    path("camera",camera, name="camera"),
]