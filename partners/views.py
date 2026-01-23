from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from partners.models import Customer, Supplier, Employee, Address
from partners.serializres import CustomerSerializer, SupplierSerializer, EmployeeSerializer, AddressSerializer

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    model = Customer
    serializer_class = CustomerSerializer
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]
    
class SupplierViewSet(viewsets.ModelViewSet):
    model = Supplier
    serializer_class = SupplierSerializer
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    model = Employee
    serializer_class = EmployeeSerializer
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]

class AddressViewSet(viewsets.ModelViewSet):
    model = Address
    serializer_class = AddressSerializer
    queryset = model.objects.all()
    permission_classes = [IsAuthenticated]