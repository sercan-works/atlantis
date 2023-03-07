from django.shortcuts import render,redirect
from django.contrib import messages
from envanter.forms import RamForm
from .models import Ram

def post_list(request):
    qs = Ram.objects.all()
    context = {
        'object_list' : qs
    }
    return render (request, "envanter/post_list.html", context )

def ram_create(request):
    form = RamForm()
    if request.method == "POST":
        form = RamForm(request.POST)
        # print(request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Ram created successfully!")
            return redirect("envanter:list")
    context = {
        'form' : form
    }
    return render (request, "envanter/ram_create.html", context)
