
from django.urls import path

from envanter.views import post_list

app_name = "envanter"

urlpatterns = [
    path("",post_list, name="list"),
]