from django.urls import path
from . import views

urlpatterns =[
    path ('berita/', views.berita, name='berita'),
]

