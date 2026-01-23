from django.contrib import admin
from partners.models import Customer, Supplier, Employee, Address
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'is_active')
    search_fields = ('name', 'email', 'document')
    list_filter = ('is_active',)
    
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'document', 'phone', 'email', 'is_active')
    search_fields = ('name', 'document', 'email')
    list_filter = ('is_active',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'document', 'role', 'salary', 'hire_date', 'termination_date', 'is_active')
    search_fields = ('user__username', 'document', 'role')
    list_filter = ('is_active', 'role')
    
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'number', 'city', 'state', 'zip_code', 'country')
    search_fields = ('street', 'city', 'state', 'country')
