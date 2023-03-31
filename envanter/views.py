from django.shortcuts import render,redirect
from django.contrib import messages
from envanter.forms import RamForm,PcForm
from .models import Ram,PC

def post_list(request):
    all_pc = PC.objects.all()
    context = {
        'object_list' : all_pc
    }
    return render (request, "envanter/index.html", context )

def pc_create(request):
    form = PcForm()
    if request.method == "POST":
        form = PcForm(request.POST)
        # print(request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "PC created successfully!")
            return redirect("envanter:list")
    context = {
        'form' : form
    }
    return render (request, "envanter/pc_create.html", context)

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
