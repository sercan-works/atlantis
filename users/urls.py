from django.urls import path, include
from .views import RegisterAPI,StaffCheckView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterAPI.as_view()),
    path("staff_check/", StaffCheckView.as_view()),

]
