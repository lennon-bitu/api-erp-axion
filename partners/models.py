from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    document = models.CharField(max_length=18, blank=True)
    address = models.ForeignKey('partners.Address', on_delete=models.SET_NULL, null=True, blank=True, related_name='customers')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    document = models.CharField(max_length=18)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.ForeignKey('partners.Address', on_delete=models.SET_NULL, null=True, blank=True, related_name='suppliers')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class Employee(models.Model):
    user = models.OneToOneField('core.User', on_delete=models.CASCADE)
    document = models.CharField(max_length=18, unique=True, null=True, blank=True)
    role = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    termination_date = models.DateField(null=True, blank=True)
    address = models.ForeignKey('partners.Address', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'


class Address(models.Model):
    street = models.CharField(max_length=150, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    neighborhood = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
