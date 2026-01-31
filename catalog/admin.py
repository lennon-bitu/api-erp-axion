from django.contrib import admin
from .models import Product, ProductImage, ProductVariation, Category


# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 5


class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_active')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'sku')

    inlines = [
        ProductImageInline,
        ProductVariationInline
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
