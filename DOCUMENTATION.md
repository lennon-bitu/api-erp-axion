# 📦 Documentação de Estrutura – SaaS de Delivery (Django)

## 1. Visão Geral do Sistema

O sistema será um **SaaS Multi-Estabelecimento** para delivery, onde:

- Cada **estabelecimento** possui seu próprio painel  
- O dono escolhe um **plano de contratação**  
- Existe um **período de teste gratuito de 7 dias**  
- O catálogo é **público** (sem login)  
- O painel é **privado** (com login e permissões)  

---

## 2. Arquitetura Geral

```
[SaaS Admin]
   └── Gerencia planos, assinaturas e estabelecimentos

[Estabelecimento]
   ├── Produtos
   ├── Categorias
   ├── Pedidos
   ├── Clientes
   ├── Relatórios
   └── Configurações

[Catálogo Público]
   └── /public/catalog/<slug>/
```

---

## 3. Estrutura de Apps (Django)

| App | Responsabilidade |
|-----|------------------|
| core | Configurações globais, utilitários |
| users | Usuários, autenticação, papéis |
| tenants | Estabelecimentos (empresas) |
| plans | Planos, preços e limites |
| subscriptions | Assinaturas e período de teste |
| products | Produtos e categorias |
| orders | Pedidos e itens |
| customers | Clientes finais |
| payments | Integrações (Pix, Stripe, etc.) |
| public | Catálogo público |

---

## 4. Modelo de Estabelecimento (Tenant)

Cada empresa cadastrada no SaaS será um **Tenant**.

### Campos principais

```
Tenant
- name
- slug
- cnpj
- phone
- email
- address
- logo
- banner
- is_active
- created_at
```

---

## 5. Estrutura de Planos

### Planos sugeridos

| Plano | Produtos | Pedidos | Recursos |
|------|----------|---------|----------|
| Start | 50 | 300/mês | Básico |
| Premium | 200 | Ilimitado | Relatórios |
| Diamond | Ilimitado | Ilimitado | Integrações + API |

### Model

```
Plan
- name
- price
- max_products
- max_orders
- features (JSON)
```

---

## 6. Assinaturas e Teste Grátis (7 dias)

Todo novo estabelecimento recebe:

- **7 dias de teste gratuito**
- Sem necessidade de pagamento inicial

### Model

```
Subscription
- tenant
- plan
- status (trial, active, canceled)
- trial_end
- start_date
- end_date
```

### Regra de acesso

```
Se hoje <= trial_end:
    acesso liberado
Senão:
    exigir pagamento
```

---

## 7. Painel do SaaS (Admin Global)

Funcionalidades:

- Cadastro de planos
- Gerenciamento de estabelecimentos
- Controle de assinaturas
- Relatórios financeiros
- Configuração de pagamentos
- Métricas de uso

Rotas:

```
/saas/dashboard/
/saas/plans/
/saas/tenants/
/saas/subscriptions/
/saas/reports/
```

---

## 8. Painel do Estabelecimento

Módulos:

### Produtos
- Categorias
- Produtos
- Estoque
- Preços

### Pedidos
- Novo pedido
- Status (Recebido, Preparando, Entregue)
- Histórico

### Clientes
- Cadastro
- Histórico de pedidos

### Relatórios
- Vendas
- Produtos mais vendidos
- Faturamento

### Configurações
- Dados da empresa
- Horários
- Taxas de entrega
- Pagamentos

Rotas:

```
/dashboard/
/dashboard/products/
/dashboard/orders/
/dashboard/customers/
/dashboard/reports/
/dashboard/settings/
```

---

## 9. Catálogo Público

Acessível sem login:

```
/public/catalog/<slug>/
```

Funcionalidades:

- Lista de categorias
- Produtos
- Carrinho
- Finalizar pedido via WhatsApp ou sistema

---

## 10. Fluxo de Cadastro

1. Usuário cria conta  
2. Cadastra estabelecimento  
3. Escolhe plano  
4. Ativa teste grátis (7 dias)  
5. Recebe acesso ao painel  
6. Publica catálogo  

---

## 11. Controle de Permissões

| Papel | Acesso |
|-------|--------|
| SaaS Admin | Tudo |
| Dono da Loja | Gestão completa |
| Funcionário | Pedidos e produtos |
| Cliente | Apenas catálogo |

---

## 12. Segurança

- Autenticação JWT ou Session
- Isolamento por Tenant
- Middleware de verificação de assinatura
- Bloqueio após fim do trial

---

## 13. Tecnologias

- Django  
- Django Rest Framework  
- PostgreSQL  
- Redis  
- Stripe / Pix  
- Celery  
- Docker  

---

## 14. Estrutura de Pastas

```
project/
│
├── core/
├── users/
├── tenants/
├── plans/
├── subscriptions/
├── products/
├── orders/
├── public/
├── templates/
└── static/
```

---

## 15. Próximos Passos

1. Criar models base
2. Implementar autenticação
3. Criar middleware de plano
4. Desenvolver painel
5. Criar catálogo público
6. Integrar pagamentos
