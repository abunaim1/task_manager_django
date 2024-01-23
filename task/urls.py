from django.urls import path
from . import views
urlpatterns = [
    path('add_task/', views.task, name='task'),
]
