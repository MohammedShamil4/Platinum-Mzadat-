"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from web import views

from django.urls import path
from . import views

from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('saleitems/add/', views.add_saleitem, name='add_saleitem'),
    path('saleitems/', views.list_saleitems, name='list_saleitems'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/', views.list_orders, name='list_orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
]