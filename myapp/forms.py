from django import forms
from myapp.models import Customer, Service, CustomerOrder


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'cost', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['customer', 'service', 'cost']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model=Customer
#         fields=['CustomerName', 'phone', 'email']
#         widgets = { 'CustomerName': forms.TextInput(attrs={ 'class': 'form-control' }), 
#             'phone': forms.TextInput(attrs={ 'class': 'form-control' }),
#             'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
#         }

# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model=Service
#         fields=['NameOfService', 'cost', 'description']
#         widgets = { 'NameOfService': forms.TextInput(attrs={ 'class': 'form-control' }), 
#             'cost': forms.NumberInput(attrs={ 'class': 'form-control' }),
#             'description': forms.TextInput(attrs={ 'class': 'form-control' }),
#         }

# class CustomerOrderForm(forms.ModelForm):
#     class Meta:
#         model=CustomerOrder
#         fields=['CustomerName', 'phone', 'email','cost','NameOfService']
#         widgets = { 'CustomerName': forms.TextInput(attrs={ 'class': 'form-control' }), 
#             'phone': forms.TextInput(attrs={ 'class': 'form-control' }),
#             'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
#             'cost': forms.NumberInput(attrs={ 'class': 'form-control' }),
#             'NameOfService': forms.TextInput(attrs={ 'class': 'form-control' }),
#         }
