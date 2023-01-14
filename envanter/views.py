from django.shortcuts import render
from .models import Ram

def post_list(request):
    qs = Ram.objects.all()
    context = {
        'object_list' : qs
    }
    return render (request, "envanter/post_list.html", context )
