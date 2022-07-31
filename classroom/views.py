from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ContactForm
from .models import Teacher

# def home_view(request):
#     return render(request, 'classroom/home.html')


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankView(TemplateView):
    template_name = 'classroom/thanks.html'


class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    # auto trigger .save()
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank')


class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    # model_list.html
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher
    # model_detail.html
    context_object_name = 'teacher'


class TeacherUpdateView(UpdateView):
    model = Teacher
    # SHARE model_form.html --- PK
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    # FORM --> Confirm Delete Button
    model = Teacher
    # model_confirm_delete.html
    success_url = reverse_lazy('classroom:list_teacher')
    context_object_name = 'teacher'


class ContextFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # URL, NOT Templates
    success_url = reverse_lazy('classroom:thank')

    def form_valid(self, form):
        print(form.cleaned_data)
        # ContactForm(request.POST)
        return super().form_valid(form)

