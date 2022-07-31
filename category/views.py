from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from .models import Book, Genre, Language, BookInstance, Author
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


def index(request):
    num_book = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        "num_book": num_book,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
    }

    return render(request, 'category/index.html', context=context)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'


class BookDetail(DetailView):
    model = Book


@login_required
def my_view(request):
    return render(request, 'category/my_view.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'category/signup.html'


class CheckOutBooksByUserView(LoginRequiredMixin, ListView):
    # List all BookInstances but I will filter based off currently logged in user session
    model = BookInstance
    template_name = 'category/profile.html'
    paginate_by = 5 # 5 book instances per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
