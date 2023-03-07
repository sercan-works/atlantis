
from django.urls import path

from envanter.views import post_list,ram_create

app_name = "envanter"

urlpatterns = [
    path("",post_list, name="list"),
    path("create/ram",ram_create, name="ram_create"),
]