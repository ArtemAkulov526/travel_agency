"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp.views import customer_list, service_list, customerorders_list, CustomerNewForm, ServiceNewForm, CustomerOrderNewForm, get_service_cost 
from myapp.views import delete_service, delete_customer, delete_customer_order, update_customer, update_services, update_customer_orders


urlpatterns = [
    path('admin/', admin.site.urls),  

    # Customers
    path('', customer_list, name='customer_list'),
    path('customers/new/', CustomerNewForm, name='customer_new_form'),
    path('customer/update/<int:id>/', update_customer, name='customer_update'),
    path('customer/delete/<int:id>/', delete_customer, name='delete_customer'),

    # Services
    path('services/', service_list, name='services'),
    path('services/new/', ServiceNewForm, name='service_new_form'),
    path('service/update/<int:id>/', update_services, name='service_update'),
    path('service/delete/<int:id>/', delete_service, name='deleteservice'),

    # Customer Orders
    path('customerorders/', customerorders_list, name='customerorders'),
    path('orders/new/', CustomerOrderNewForm, name='customer_order_new_form'),
    path('orders/update/<int:id>/', update_customer_orders, name='update_customerorders'),
    path('orders/delete/<int:id>/', delete_customer_order, name='deletecustomerorder'),

    # AJAX
    path('ajax/service-cost/<int:service_id>/', get_service_cost, name='get_service_cost'),
]


#python manage.py runserver


