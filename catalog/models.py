from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    sku = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_margin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default=0)
    stock_control = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/')

    def save(self, *args, **kwargs):
        if self.product.images.count() >= 5 and not self.pk:
            raise ValidationError("A product can have a maximum of 5 images.")
        super().save(*args, **kwargs)


class ProductVariation(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='variations',
        on_delete=models.CASCADE
    )

    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # 🔥 atributos dinâmicos
    attributes = models.JSONField(default=dict, blank=True)   # exemplo: {"color": "Black", "size": "M", "material": "Cotton"}

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.sku}"
