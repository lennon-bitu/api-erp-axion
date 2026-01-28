# Documentação dos Serializers de Produto

Este documento descreve os serializers do módulo de produtos usando Django Rest Framework.

## CategorySerializer
Serializa categorias ativas do sistema.

Campos:
- id
- name
- is_active

## ProductImageSerializer
Serializa imagens do produto.

Campos:
- id
- image

## ProductVariationSerializer
Serializa variações do produto.

Campos:
- id (somente leitura)
- sku
- price
- stock
- attributes
- is_active
- created_at (somente leitura)

## ProductSerializer
Serializer principal responsável por criar e atualizar produtos e variações.

Campos:
- id
- name
- description
- sku
- price
- cost_price
- profit_margin
- stock
- stock_control
- category_id
- variations
- images
- is_active

### Regras
- Variações são opcionais
- Categoria aceita apenas registros ativos
- No update, variações só são alteradas se enviadas no payload
