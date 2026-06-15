# 💰 GastoCerto
🌐 **Aplicação publicada:** [https://gastocerto.onrender.com](https://gastocerto.onrender.com)
![CI](https://github.com/SEU_USUARIO/gastocerto/actions/workflows/ci.yml/badge.svg)
![Versão](https://img.shields.io/badge/versão-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9%2B-green)
![Django](https://img.shields.io/badge/django-4.2-092E20)
![Licença](https://img.shields.io/badge/licença-MIT-lightgrey)

> Gerencie seus gastos pessoais pelo navegador de forma simples e acessível.

---

## 📌 O Problema

Milhões de brasileiros enfrentam dificuldades para controlar seus gastos mensais. A ausência de acompanhamento financeiro leva ao endividamento e ao consumo impulsivo. Ferramentas complexas intimidam quem não tem familiaridade com tecnologia.

## 💡 A Solução

**GastoCerto** é uma aplicação web leve construída com Django. O usuário cadastra gastos com descrição, valor e categoria, filtra o histórico, edita ou remove lançamentos e visualiza um resumo financeiro por categoria — tudo pelo navegador, sem necessidade de cadastro ou internet externa.

## 👥 Público-Alvo

Estudantes, trabalhadores autônomos e microempreendedores que querem iniciar o controle financeiro de forma simples.

---

## ✨ Funcionalidades

| Rota              | Descrição                                        |
|-------------------|--------------------------------------------------|
| `/`               | Lista todos os gastos com total e resumo         |
| `/adicionar/`     | Formulário para cadastrar novo gasto             |
| `/editar/<id>/`   | Editar um gasto existente                        |
| `/remover/<id>/`  | Confirmar e remover um gasto                     |

**Categorias:** `Alimentação`, `Transporte`, `Saúde`, `Educação`, `Lazer`, `Moradia`, `Outros`

---

## 🛠️ Tecnologias

- **Python 3.9+**
- **Django 4.2** — framework web
- **SQLite** — banco de dados local
- **pytest + pytest-django** — testes automatizados
- **ruff** — linting e análise estática
- **GitHub Actions** — integração contínua (CI)

---

## 🚀 Instalação

### Pré-requisitos
- Python 3.9 ou superior
- Git

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/gastocerto.git
cd gastocerto

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações (cria o banco de dados)
python manage.py migrate

# 5. Inicie o servidor
python manage.py runserver
```

Acesse **http://127.0.0.1:8000** no navegador.

---

## 🧪 Executar os Testes

```bash
pytest --tb=short -v
```

Os testes cobrem:
- ✅ Criação de gasto válido
- ❌ Valor negativo e zero rejeitados
- 🔍 Filtro por categoria nas views
- 🌐 Status HTTP das páginas
- 🗑️ Remoção e redirecionamento

---

## 🔍 Executar o Lint

```bash
ruff check .
```

Para corrigir automaticamente:

```bash
ruff check . --fix
```

---

## ⚙️ CI — GitHub Actions

Pipeline executada em `push` e `pull_request` para `main`. Etapas:

1. Checkout do código
2. Configuração do Python 3.11
3. Instalação de dependências
4. Lint com `ruff`
5. Migrações com `manage.py migrate`
6. Testes com `pytest`

Arquivo: `.github/workflows/ci.yml`

---

## 📁 Estrutura do Projeto

```
gastocerto/
├── config/                    # Configuração Base
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
├── gastos/                    # Regras de Negócio
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── templates/gastos/
│   │   ├── base.html
│   │   ├── lista.html
│   │   ├── form.html
│   │   └── confirmar_remocao.html
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── tests/                     # Qualidade e Testes
│   ├── __init__.py
│   ├── test_models.py
│   └── test_views.py
├── .github/workflows/
│   └── ci.yml
├── manage.py
├── pyproject.toml
├── requirements.txt
├── VERSION
├── CHANGELOG.md
├── LICENSE
├── .gitignore
└── README.md
```

---

## 📌 Versão Atual

**1.0.0** — Consulte o [CHANGELOG](CHANGELOG.md).

---

## 👤 Autor

**Contribuição realizada por Eric Kelvin Da Silva**Eric Kelvin Da Silvadia 14/06
🔗 [github.com/SEU_USUARIO/gastocerto](https://github.com/SEU_USUARIO/gastocerto)
Contribuição realizada por Eric Kelvin Da Silva.dia 14/06## Integrantes do Grupo
* Eric Kelvin Da Silva
* [Nome do Colega 1]
* [Nome do Colega 2]

## Sobre o Projeto
* **Link do deploy:** [https://gastocerto-1.onrender.com](https://gastocerto-1.onrender.com)
* **Tecnologias usadas:** Django, PostgreSQL, Supabase, Render