# 🚀 API ERP Axion – SaaS Backend (Django + Docker)

Este projeto é um **backend SaaS** desenvolvido em **Django**, voltado para **ERP / Delivery**, utilizando **arquitetura multi-tenant**, API REST e execução totalmente via **Docker**.

---

## 🧰 Tecnologias Utilizadas

- Python 3.10+
- Django
- Django Rest Framework
- Django Simple JWT
- Django Tenants
- PostgreSQL
- Docker
- Docker Compose

---

## 📦 Funcionalidades

- Arquitetura SaaS Multi-Tenant
- Cadastro de empresas (tenants)
- Autenticação JWT
- API RESTful
- Controle de planos
- Isolamento de dados por tenant

---

## 🔽 Clonando o Projeto

```bash
git clone https://github.com/lennon-bitu/api-erp-axion.git
cd api-erp-axion
```

---

## 🐳 Execução com Docker

### Pré-requisitos

- Docker
- Docker Compose

```bash
docker --version
docker compose version
```

---

## ⚙️ Variáveis de Ambiente

Crie o arquivo `.env` na raiz do projeto:

```env
DEBUG=True
SECRET_KEY=sua_secret_key
POSTGRES_DB=axion
POSTGRES_USER=axion_user
POSTGRES_PASSWORD=senha_segura
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

## ▶️ Subindo o Ambiente

```bash
docker compose up --build
```

Modo background:

```bash
docker compose up -d --build
```

---

## 🌐 Acessando a API

```
http://localhost:8000/
```

---

## 🔐 Autenticação JWT

```http
POST /api/token/
```

```json
{
  "username": "admin",
  "password": "senha"
}
```

---

## 🌍 Multi-Tenant Local

Adicione no arquivo `hosts`:

```text
127.0.0.1 empresa1.localhost
127.0.0.1 empresa2.localhost
```

---

## 🛑 Parando Containers

```bash
docker compose down
```

Remover volumes:

```bash
docker compose down -v
```

---

## 👨‍💻 Autor

Lennon Bitu  
https://github.com/lennon-bitu
