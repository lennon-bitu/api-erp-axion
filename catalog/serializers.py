# Importa o módulo de serializers do Django Rest Framework
from rest_framework import serializers

# Importa os models que serão serializados
from .models import (
    Category,          # Modelo de categoria de produto
    Product,           # Modelo principal de produto
    ProductImage,      # Modelo de imagens do produto
    ProductVariation   # Modelo de variações do produto
)

# Serializer responsável por converter o model Category em JSON e vice-versa
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category                     # Define o model que será serializado
        fields = ['id', 'name', 'is_active'] # Campos expostos na API


# Serializer responsável pelas imagens do produto
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage        # Model de imagem do produto
        fields = ['id', 'image']    # Retorna o ID e o arquivo de imagem


# Serializer responsável pelas variações do produto
class ProductVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariation    # Model de variação
        fields = [
            'id',                   # Identificador da variação
            'sku',                  # SKU específico da variação
            'price',                # Preço da variação
            'stock',                # Estoque da variação
            'attributes',           # Atributos dinâmicos (JSONField)
            'is_active',             # Define se a variação está ativa
            'created_at'             # Data de criação
        ]
        # Define campos que não podem ser alterados via API
        read_only_fields = ['id', 'created_at']


# Serializer principal do produto
class ProductSerializer(serializers.ModelSerializer):

    # Campo de variações relacionado ao produto
    # many=True indica múltiplas variações
    # required=False torna o envio opcional
    variations = ProductVariationSerializer(
        many=True,
        required=False
    )

    # Campo de imagens relacionadas ao produto
    # read_only=True impede criação/edição direta por este serializer
    images = ProductImageSerializer(many=True, read_only=True)

    # Campo customizado para receber apenas o ID da categoria
    # source='category' faz o vínculo com o campo category do model
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(is_active=True),  # Apenas categorias ativas
        source='category'
    )

    class Meta:
        model = Product   # Model associado ao serializer
        fields = [
            'id',              # ID do produto
            'name',            # Nome do produto
            'description',     # Descrição
            'sku',             # SKU principal
            'price',           # Preço de venda
            'cost_price',      # Preço de custo
            'profit_margin',   # Margem de lucro
            'stock',           # Estoque principal
            'stock_control',   # Flag de controle de estoque
            'category_id',     # Categoria vinculada
            'variations',      # Variações do produto
            'images',          # Imagens do produto
            'is_active'        # Status do produto
        ]

    # Método sobrescrito para criação do produto
    def create(self, validated_data):
        # Remove as variações do payload principal, se existirem
        variations_data = validated_data.pop('variations', [])

        # Cria o produto com os dados restantes
        product = Product.objects.create(**validated_data)

        # Cria cada variação vinculando ao produto criado
        for variation_data in variations_data:
            ProductVariation.objects.create(
                product=product,
                **variation_data
            )

        # Retorna o produto criado
        return product
    
    # Método sobrescrito para atualização do produto
    def update(self, instance, validated_data):
        # Remove as variações do payload, se existirem
        variations_data = validated_data.pop('variations', None)

        # Atualiza os campos do produto dinamicamente
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Salva as alterações do produto
        instance.save()

        # Só altera as variações se elas vierem no payload
        if variations_data is not None:
            # Remove todas as variações antigas
            instance.variations.all().delete()

            # Cria novamente as variações enviadas
            for variation_data in variations_data:
                ProductVariation.objects.create(
                    product=instance,
                    **variation_data
                )

        # Retorna o produto atualizado
        return instance
