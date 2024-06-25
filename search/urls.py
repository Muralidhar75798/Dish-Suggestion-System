# urls.py in search application
from django.urls import path
from search import views

urlpatterns = [
    path('search/', views.search_view, name='search'),
]
