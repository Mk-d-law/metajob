from django.urls import path
from . import views

urlpatterns = [
    path('metajob_feed/', views.metajob_feed, name='metajob_feed'),
    path('metajob_generate/', views.metajob_generate, name='metajob_generate'),
    path('jobgrin_feed/', views.jobgrin_feed, name='jobgrin_feed'),
    path('jobgrin_generate/', views.jobgrin_generate, name='jobgrin_generate'),
    path('indeed_feed/', views.indeed_feed, name='indeed_feed'),
    path('indeed_generate/', views.indeed_generate, name='indeed_generate'),
    path('adzuna_feed/', views.adzuna_feed, name='adzuna_feed'),
    path('adzuna_generate/', views.adzuna_generate, name='adzuna_generate'),
    
]
