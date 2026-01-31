from django.db import models
from django.core.exceptions import ValidationError
from catalog.models import Product, ProductVariation


class Stock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="stocks"
    )

    variation = models.OneToOneField(
        ProductVariation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="stock"
    )

    quantity = models.IntegerField(default=0)

    def clean(self):
        """
        Regras:
        - Estoque deve pertencer a Product OU ProductVariation
        - Nunca aos dois
        - Produto só pode ter estoque direto se NÃO tiver variações
        """
        if not self.product and not self.variation:
            raise ValidationError(
                "O estoque deve estar vinculado a um produto ou a uma variação."
            )

        if self.product and self.variation:
            raise ValidationError(
                "O estoque não pode estar vinculado a produto e variação ao mesmo tempo."
            )

        if self.product and self.product.variations.exists():
            raise ValidationError(
                "Produtos com variações não podem ter estoque direto."
            )

    def __str__(self):
        if self.variation:
            return f"Stock - {self.variation}"
        return f"Stock - {self.product}"


class StockMovement(models.Model):
    MOVEMENT_TYPE = (
        ('in', 'Entrada'),
        ('out', 'Saída'),
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    variation = models.ForeignKey(
        ProductVariation,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    quantity = models.PositiveIntegerField()
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPE)

    origin = models.CharField(
        max_length=50,
        help_text="Ex: compra, venda, ajuste, devolução"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.product and not self.variation:
            raise ValidationError(
                "O movimento deve estar vinculado a um produto ou variação."
            )

        if self.product and self.variation:
            raise ValidationError(
                "O movimento não pode estar vinculado a produto e variação ao mesmo tempo."
            )

    def __str__(self):
        target = self.variation or self.product
        return f"{self.get_movement_type_display()} - {target}"
