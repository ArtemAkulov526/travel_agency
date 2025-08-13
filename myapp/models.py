from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'services'

    def __str__(self):
        return self.name


class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='orders')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'customerorders'

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"


# class Customer(models.Model):
#     CustomerId = models.AutoField(primary_key=True)
#     CustomerName = models.CharField(max_length=255)
#     phone = models.CharField(max_length=13)
#     email = models.EmailField()

#     class Meta:
#         db_table= 'customers'


# class Service(models.Model):
#     ServiceId= models.AutoField(primary_key=True)
#     NameOfService = models.CharField(max_length=255)
#     cost=models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.CharField(max_length=255)

#     class Meta:
#         db_table= 'services'


# class CustomerOrder(models.Model):
#     OrderId= models.AutoField(primary_key=True)
#     CustomerName = models.CharField(max_length=255)
#     phone = models.CharField(max_length=13)
#     email = models.EmailField(max_length=35)
#     cost= models.DecimalField(max_digits=10, decimal_places=2)
#     NameOfService = models.CharField(max_length=255)

#     class Meta:
#         db_table= 'customerorders'







