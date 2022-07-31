from django.shortcuts import render, redirect
from django.urls import reverse
from . import models


def list_view(request):
    all_cars = models.Car.objects.all()
    context_all_cars = {'all_cars': all_cars}
    return render(request, 'cars/list.html', context=context_all_cars)


def add_view(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        # if user submitted a car --> list.html
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')


def delete_view(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            error_message = {'error': "PK not found !!!"}
            return render(request, 'cars/delete.html', context=error_message)
    else:
        return render(request, 'cars/delete.html')
