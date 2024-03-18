from django.urls import path
from .views import *

urlpatterns = [
    path('', lessons, name='lessons'),
    path('add/', add_lesson, name='add'),
    path('delete_lesson/<int:id>/', delete_lesson, name='delete_lesson'),
    path('edit_lesson/<int:id>/', edit_lesson, name='edit_lesson'),
]
