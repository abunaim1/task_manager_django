from django.urls import path
from . import views
urlpatterns = [
    path('add_category/', views.category, name='category'),
]
