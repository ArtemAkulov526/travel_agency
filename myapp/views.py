from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from myapp.models import Customer, Service, CustomerOrder
from myapp.forms import CustomerForm, ServiceForm, CustomerOrderForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def customerorders_list(request):
    customerorders = CustomerOrder.objects.all()
    return render(request, 'customerorders.html', {'customerorders': customerorders})

def CustomerNewForm(request):
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('customer_list')  
            except:  
                pass
    else:  
         form=CustomerForm()
    return render(request,'customer_new_form.html', {'form': form})


def ServiceNewForm(request):
    if request.method == "POST":  
        form = ServiceForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('services')  
            except:  
                pass
    else:  
         form=ServiceForm()
    return render(request,'service_new_form.html', {'form': form})

def CustomerOrderNewForm(request):
    if request.method == "POST":  
        form = CustomerOrderForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
         form=CustomerOrderForm()
    return render(request,'customer_order_new_form.html', {'form': form})

def delete_customer_order(request, id):  
    orderid = CustomerOrder.objects.get(pk=id)  
    orderid.delete()  
    return redirect('customerorders')

def delete_customer(request, id):  
    customerid = Customer.objects.get(pk=id)  
    customerid.delete()  
    return redirect('customer_list')  

def delete_service(request, id):  
    serviceid = Service.objects.get(pk=id)  
    serviceid.delete()  
    return redirect("services")  

def update_customer(request, id):  
    customer = get_object_or_404(Customer, id=id)  

    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():  
        try:  
            form.save()  
            return redirect('customer_list')  
        except Exception as e:
            print(e)

    return render(request, 'customer_update.html', {'customer': customer, "form": form})

def update_services(request, id):  
    services = Service.objects.get(pk=id)  
    form=ServiceForm(request.POST or None, instance=services)
    if form.is_valid():  
            try:  
                form.save()  
                return redirect('services')  
            except:  
                pass
    return render(request,'service_update.html', {'services': services, "form":form })

def update_customer_orders(request, id):  
    customerorders = CustomerOrder.objects.get(pk=id)  
    form=CustomerOrderForm(request.POST or None, instance=customerorders)
    if form.is_valid():  
            try:  
                form.save()  
                return redirect('customerorders')  
            except:  
                pass
    return render(request,'update_customer_orders.html', {'customerorders': customerorders, "form":form })

def get_service_cost(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        return JsonResponse({'cost': str(service.cost)})
    except Service.DoesNotExist:
        return JsonResponse({'cost': ''})