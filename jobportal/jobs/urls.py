from django.urls import path
from . import views

urlpatterns = [
    path('job_feed/', views.job_feed, name='job_feed'),
]
