"""
URL configuration for webberita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from berita.views import *

urlpatterns = [
    path('', include('berita.urls')),
    path('', berita, name='berita'),
    path('add/', add, name='add'),
    path('addrec/', addrec, name='addrec'),
    path('delete/<int:id>/', delete, name='delete'), 
    path('update/<int:id>/',update,name='update'),
    path('update/uprec/<int:id>/',uprec,name='uprec'),

    path('detailberita/', detailberita, name='detailberita'),
    path('isiberita/', isiberita, name='isiberita'),
    path('done/', done, name='done'),
    path('formberita/', formberita, name='formberita'),
    path('admin/', admin.site.urls),
]
