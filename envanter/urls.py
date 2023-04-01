
from django.urls import path

from envanter.views import post_list,ram_create,pc_create,pc_edit

app_name = "envanter"

urlpatterns = [
    path("",post_list, name="list"),
    path("create/pc", pc_create, name="pc_create"),
    path("update/pc/<int:id>", pc_edit, name="pc_edit"),
    path("create/ram",ram_create, name="ram_create"),
    
]