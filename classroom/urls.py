from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank/', views.ThankView.as_view(), name='thank'),
    path('contact/', views.ContextFormView.as_view(), name='contact'),
    path('create_teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
    path('list_teacher/', views.TeacherListView.as_view(), name='list_teacher'),
    path('detail_teacher/<int:pk>', views.TeacherDetailView.as_view(), name='detail_teacher'),
    path('update_teacher/<int:pk>', views.TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', views.TeacherDeleteView.as_view(), name='delete_teacher'),
]