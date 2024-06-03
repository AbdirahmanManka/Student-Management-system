from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_number>/', views.view_student, name='view_student'),  # Change 'id' to 'student_number'
    path('add/', views.add, name='add'),
    path('edit/<int:student_number>/', views.edit, name='edit'),  # Change 'id' to 'student_number'
    path('delete/<int:student_number>/', views.delete, name='delete')  # Change 'id' to 'student_number'
    
]
