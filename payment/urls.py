from django.urls import path
from . import views

urlpatterns = [
    path('status', views.uptimeHandler),
]
