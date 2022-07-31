from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm


def rental_view(request):

    # POST REQUEST --> FORM CONTENT --> THANK
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('phones:thank'))
    else:
        form = ReviewForm()
    return render(request, 'phones/rental_review.html', context={'form':form})


def thank_view(request):
    return render(request, 'phones/thank.html')