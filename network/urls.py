from django.urls import path

from network.views import ping_page

app_name = "network"

urlpatterns = [
    path("",ping_page, name="ping"),
]