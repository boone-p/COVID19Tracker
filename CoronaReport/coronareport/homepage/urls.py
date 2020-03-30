from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='homepage-about'),
    path('report/', views.report, name='homepage-report'),

]
