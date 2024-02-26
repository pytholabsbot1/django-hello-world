# example/urls.py
from django.urls import path

from .views import home_view

urlpatterns = [
    # ... other patterns...
    path('', home_view, name='home'),
]