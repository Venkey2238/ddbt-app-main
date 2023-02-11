"""Project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name = 'index'),
   path('AddPeer', views.AddPeer, name = 'AddPeer'),
   path('AddToBlock', views.AddToBlock, name = 'AddToBlock'),
   path('Transactions', views.Transactions, name = 'Transactions'),
   path('ViewChain', views.ViewChain, name = 'ViewChain'),
   path('signup', views.signup, name = 'signup'),
   path("AddPeerAction", views.AddPeerAction, name="AddPeerAction"),
   path("BlockAdded", views.BlockAdded, name="BlockAdded"),
   path("TransactionsSubmit", views.TransactionsSubmit, name="TransactionsSubmit"),
 

]
