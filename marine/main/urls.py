from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Homepage 1 (slider)
    path('home1/', views.home, name='home1'),   # Optional
    path('home2/', views.home2, name='home2'),  # Homepage 2 (single video)
    path('home3/', views.home3, name='home3'),

]
