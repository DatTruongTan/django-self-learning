from django.shortcuts import render
from . import models


def list_patients(request):
    all_patients = models.Patient.objects.all()
    context_all_patients = {'patients': all_patients}
    return render(request, 'office/list.html', context=context_all_patients)
