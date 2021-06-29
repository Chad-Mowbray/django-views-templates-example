from django.urls import path
from .views import practice

urlpatterns = [
    path('practice/', practice )
]