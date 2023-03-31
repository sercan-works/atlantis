
from django.urls import path

from envanter.views import post_list,ram_create,pc_create

app_name = "envanter"

urlpatterns = [
    path("",post_list, name="list"),
    path("create/pc", pc_create, name="pc_create"),
    path("create/ram",ram_create, name="ram_create"),
    
]