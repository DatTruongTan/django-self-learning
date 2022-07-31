from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def not_found_view(request, exception):
    return render(request, 'error.html', status=404)
