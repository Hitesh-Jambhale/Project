from django.shortcuts import render, redirect
from .models import Laptop
from .forms import LaptopModelForm
from django.contrib import messages


def home_view(request):
    laptops = Laptop.objects.all()
    return render(request, template_name='myapp/home.html', context={'laptops': laptops})


def create_view(request):
    form = LaptopModelForm()
    if request.method == "POST":
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Entry Is Added Successfully!.')
            return redirect('homepage')
    return render(request, template_name='myapp/form.html', context={'form': form})


def update_view(request, pk):
    entry = Laptop.objects.get(id=pk)
    form = LaptopModelForm(instance=entry)
    if request.method == "POST":
        form = LaptopModelForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Entry was updated.')
            return redirect('homepage')
    return render(request, template_name='myapp/form.html', context={'form': form})


def delete_view(request, pk):
    laptop = Laptop.objects.get(id=pk)
    if request.method == "POST":
        laptop.delete()
        messages.success(request, f'Your Entry was deleted.')
        return redirect('homepage')
    return render(request, template_name='myapp/deletepage.html', context={'laptop': laptop})
