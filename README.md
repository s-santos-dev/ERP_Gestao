# ERP_Gestao

Sistema ERP (Enterprise Resource Planning) multi-tenant desenvolvido em Django, com arquitetura baseada em **Service Layer + Repository Pattern (Selectors)**. Cada empresa cadastrada funciona como um *tenant* isolado, com controle de usuários, permissões por módulo e auditoria de alterações.

## Funcionalidades

- **Autenticação de usuários** com modelo customizado (login via e-mail) e dashboard.
- **Gestão de empresas (tenants)**: cadastro, edição, listagem e desativação, com dados de razão social, CNPJ, endereço, contato e identidade visual (logo e cores).
- **Módulos configuráveis por empresa**: Vendas, Compras, Estoque e Financeiro (habilitáveis individualmente).
- **Permissões granulares por usuário**: vender, comprar, gerenciar estoque, ver financeiro, gerenciar usuários.
- **Auditoria**: middleware e app dedicados ao registro de ações realizadas no sistema.
- **Modelo base reutilizável** (`BaseModel`) com UUID como chave primária, timestamps, soft-delete (`ativo`) e vínculo obrigatório com empresa/usuário criador.

## Tecnologias utilizadas

| Categoria | Tecnologia |
|---|---|
| Linguagem | Python |
| Framework web | Django (>=4.2, <5.0) |
| Banco de dados | SQLite (desenvolvimento) / PostgreSQL (produção, via `psycopg2-binary`) |
| Templates | Django Templates + HTML |
| Estilização de formulários | django-crispy-forms + crispy-bootstrap5 (Bootstrap 5) |
| Configuração de ambiente | python-decouple (variáveis via `.env`) |
| Filtros | django-filter |
| Imagens | Pillow |
| Servidor WSGI (produção) | Gunicorn |
| Cache/filas (produção) | Redis |
| Monitoramento de erros (produção) | Sentry SDK |
| Ferramentas de desenvolvimento | django-debug-toolbar, django-extensions |
| Testes | pytest-django, coverage |
| Qualidade de código | black, isort, flake8 |

## Estrutura do projeto

```
ERP_Gestao/
├── apps/
│   ├── core/          # Modelos base, mixins e utilitários compartilhados
│   ├── empresas/      # Gestão de empresas (tenants)
│   ├── usuarios/      # Usuário customizado, login e dashboard
│   └── auditoria/     # Middleware e serviços de auditoria
├── config/
│   ├── settings/       # base.py, development.py, production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── static/
├── templates/
├── .env.example
└── manage.py
```

## Como rodar na sua máquina

### Pré-requisitos

- Python 3.10+ instalado
- Git

### Passo a passo

1. **Clone o repositório**

   ```bash
   git clone https://github.com/s-santos-dev/ERP_Gestao.git
   cd ERP_Gestao
   ```

2. **Crie e ative um ambiente virtual**

   ```bash
   python -m venv venv

   # Linux/Mac
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

3. **Instale as dependências de desenvolvimento**

   ```bash
   pip install -r requirements/development.txt
   ```

4. **Configure as variáveis de ambiente**

   Copie o arquivo de exemplo e ajuste os valores conforme necessário:

   ```bash
   cp .env.example .env
   ```

   Conteúdo esperado do `.env` (chave `SECRET_KEY` é obrigatória mesmo em desenvolvimento):

   ```
   DEBUG=True
   SECRET_KEY=sua-chave-secreta-aqui
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_NAME=erp_gestao
   DB_USER=erp_user
   DB_PASSWORD=senha_forte
   DB_HOST=localhost
   DB_PORT=5432
   ```

   > Em desenvolvimento o banco padrão é **SQLite** (`db_dev.sqlite3`), então as variáveis de banco (`DB_*`) só são realmente necessárias ao rodar em modo produção com PostgreSQL.

5. **Defina o módulo de settings de desenvolvimento**

   ```bash
   # Linux/Mac
   export DJANGO_SETTINGS_MODULE=config.settings.development

   # Windows (PowerShell)
   $env:DJANGO_SETTINGS_MODULE="config.settings.development"
   ```

6. **Aplique as migrações do banco de dados**

   ```bash
   python manage.py migrate --settings=config.settings.development
   ```

7. **Crie um superusuário (para acessar o admin e o dashboard)**

   ```bash
   python manage.py createsuperuser --settings=config.settings.development
   ```

8. **Rode o servidor de desenvolvimento**

   ```bash
   python manage.py runserver --settings=config.settings.development
   ```

9. **Acesse a aplicação**

   - Aplicação: http://127.0.0.1:8000/
   - Login: http://127.0.0.1:8000/login/
   - Admin: http://127.0.0.1:8000/admin/

> Dica: se preferir não passar `--settings` em todo comando, exporte a variável `DJANGO_SETTINGS_MODULE=config.settings.development` no seu shell (passo 5) — assim os comandos do `manage.py` usam essa configuração por padrão.

## Colaboradores

Este projeto é fruto do trabalho em equipe de:

- **[Simão (s-santos-dev)](https://github.com/s-santos-dev)** — criador e mantenedor do repositório, responsável pela estrutura inicial do projeto e configuração do Django.
- **[Enio Jones Porto](https://github.com/eniojones07)** — colaborador, com contribuições de correção e ajustes de código via pull request.

Contribuições são bem-vindas! Para colaborar, faça um fork do projeto, crie uma branch para sua feature/correção e abra um pull request.

## Licença

Não há um arquivo de licença definido neste repositório até o momento.
