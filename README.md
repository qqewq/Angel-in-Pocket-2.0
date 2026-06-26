# Angel‑in‑Pocket 2.0  
# Ангел‑в‑кармане 2.0

Central decision‑making agent with GRA stability integration.  
Центральный агент принятия решений с интеграцией устойчивости через GRA.

***

## EN · Overview

Angel‑in‑Pocket 2.0 is a **central AI agent** that orchestrates business, science, production and arts through a unified decision‑making core. It integrates the **GRA‑Core: Unified Hierarchical Stability Library** as a backend to evaluate scenarios, detect contradictions and nullify unstable branches. [zenodo](https://zenodo.org/records/20569921)

The repository is structured as a **monorepo** with dedicated modules for:

- core Angel agent (`angel/`)
- business logic and arbitrage (“buy cheaper, sell higher”) (`business/`)
- finance, accounting, and taxes (`finance/`)
- subscriptions and billing (`billing/`)
- production and operations (`production/`)
- science and data‑driven reasoning (`science/`)
- arts and creative agents (`arts/`)
- backend API (`backend/`)
- frontend dashboard (`frontend/`)
- GRA integration layer (`gra_integration/`)
- tooling, tests, config, and Docker setup (`tools/`, `tests/`, `config/`, `docker/`) .

***

## RU · Обзор

Angel‑in‑Pocket 2.0 — это **центральный ИИ‑агент**, который управляет бизнесом, наукой, производством и искусством через единое ядро принятия решений. В качестве бэкенда устойчивости он интегрирует **GRA‑Core: Unified Hierarchical Stability Library**, чтобы оценивать сценарии, находить противоречия и обнулять нестабильные ветви. [zenodo](https://zenodo.org/records/20569921)

Репозиторий организован как **монорепо** с отдельными модулями для:

- базового ангельского агента (`angel/`)
- бизнес‑логики и арбитража («купить дешевле, продать дороже») (`business/`)
- финансов, бухгалтерии и налогов (`finance/`)
- подписок и биллинга (`billing/`)
- производства и операционных процессов (`production/`)
- науки и анализа данных (`science/`)
- искусства и творческих агентов (`arts/`)
- бэкенд‑API (`backend/`)
- фронтенд‑дашборда (`frontend/`)
- слоя интеграции с GRA (`gra_integration/`)
- утилит, тестов, конфигов и Docker‑окружения (`tools/`, `tests/`, `config/`, `docker/`) .

***

## EN · Key Components

- **Angel core (`angel/`)**  
  Central planner and coordinator. Receives goals (business, scientific, creative), constructs scenarios, and calls GRA‑Core to rank and stabilize them.

- **Business (`business/`)**  
  Modules for pricing, arbitrage, marketing, sales funnels, tactical and strategic planning.

- **Finance (`finance/`)**  
  Accounting models, basic ledgers, income/expense tracking, tax regime scaffolding.

- **Billing and subscriptions (`billing/`)**  
  Stripe/PayPal/crypto integration, plan management, MRR/ARR, churn handling and retention logic.

- **Production (`production/`)**  
  Planning, procurement, cost calculation and operational workflows.

- **Science (`science/`)**  
  Data analysis, hypothesis generation and evaluation, symbolic regression and experiment coordination.

- **Arts (`arts/`)**  
  Agents for music, visual art and text, curation tools and aesthetic scoring.

- **Backend (`backend/`)**  
  FastAPI‑style server exposing REST endpoints for projects, agents, subscriptions, stability metrics.

- **Frontend (`frontend/`)**  
  Minimal dashboard for monitoring projects, finances, subscriptions and GRA stability reports .

***

## RU · Основные компоненты

- **Ядро ангела (`angel/`)**  
  Центральный планировщик и координатор. Принимает цели (бизнес, наука, творчество), строит сценарии и вызывает GRA‑Core для их ранжирования и стабилизации.

- **Бизнес (`business/`)**  
  Модули для ценообразования, арбитража, маркетинга, продаж, тактического и стратегического планирования.

- **Финансы (`finance/`)**  
  Модели бухгалтерии, базовый учёт, доходы/расходы, каркас налоговых режимов.

- **Биллинг и подписки (`billing/`)**  
  Интеграция Stripe/PayPal/крипто, управление тарифами, MRR/ARR, работа с оттоком и удержанием.

- **Производство (`production/`)**  
  Планирование, закупки, расчёт себестоимости и операционные процессы.

- **Наука (`science/`)**  
  Анализ данных, генерация и проверка гипотез, symbolic regression, координация экспериментов.

- **Искусство (`arts/`)**  
  Агенты для музыки, визуального искусства и текста, инструменты кураторства и оценки эстетики.

- **Бэкенд (`backend/`)**  
  Сервер в стиле FastAPI с REST‑эндпоинтами для проектов, агентов, подписок и метрик устойчивости.

- **Фронтенд (`frontend/`)**  
  Минимальный дашборд для мониторинга проектов, финансов, подписок и отчётов GRA‑устойчивости .

***

## EN · GRA‑Core Integration

Angel‑in‑Pocket 2.0 treats GRA‑Core as a **stability oracle**:

- `gra_core` is added as a Git submodule:  
  `git submodule add https://github.com/qqewq/GRA-Core-new-Unified-Hierarchical-Stability-Library gra_core`. [zenodo](https://zenodo.org/records/20569921)
- `gra_integration/` provides:
  - client classes for calling GRA metrics and nullification routines,
  - scenario evaluation APIs for business, science and arts,
  - unified stability reports that feed back into the Angel planner.

All high‑impact decisions (pricing, strategy, experiments, creative campaigns) are passed through GRA evaluation before they are applied.

***

## RU · Интеграция с GRA‑Core

Angel‑in‑Pocket 2.0 воспринимает GRA‑Core как **оракул устойчивости**:

- `gra_core` добавляется как Git‑подмодуль:  
  `git submodule add https://github.com/qqewq/GRA-Core-new-Unified-Hierarchical-Stability-Library gra_core`. [zenodo](https://zenodo.org/records/20569921)
- В `gra_integration/` находятся:
  - клиентские классы для вызова метрик GRA и процедур обнуления,
  - API оценки сценариев для бизнеса, науки и искусства,
  - единые отчёты устойчивости, которые возвращаются в планировщик ангела.

Все решения с высоким влиянием (цены, стратегии, эксперименты, творческие кампании) пропускаются через оценку GRA перед применением.

***

## EN · Setup

From the repository root:

1. **Clone and add GRA‑Core submodule**

```bash
git clone https://github.com/qqewq/Angel-in-Pocket-2.0.git
cd Angel-in-Pocket-2.0
git submodule add https://github.com/qqewq/GRA-Core-new-Unified-Hierarchical-Stability-Library gra_core
git submodule update --init --recursive
```

2. **Create virtual environment and install dependencies**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

3. **Configure environment variables**

```bash
cp config/.env.example .env
# edit .env with API keys, DB credentials and GRA settings
```

4. **Run database migrations (if using ORM)**

```bash
alembic upgrade head
```

5. **Start the backend server**

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

6. **Open dashboard**

Visit `http://localhost:8000/dashboard/` in your browser .

7. **Docker alternative**

```bash
docker-compose -f docker/docker-compose.yml up --build
```

***

## RU · Установка и запуск

Из корня репозитория:

1. **Клонируйте репо и добавьте GRA‑Core как подмодуль**

```bash
git clone https://github.com/qqewq/Angel-in-Pocket-2.0.git
cd Angel-in-Pocket-2.0
git submodule add https://github.com/qqewq/GRA-Core-new-Unified-Hierarchical-Stability-Library gra_core
git submodule update --init --recursive
```

2. **Создайте виртуальное окружение и установите зависимости**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

3. **Настройте переменные окружения**

```bash
cp config/.env.example .env
# отредактируйте .env: ключи API, доступ к БД, настройки GRA
```

4. **Запустите миграции базы данных (если используется ORM)**

```bash
alembic upgrade head
```

5. **Запустите бэкенд‑сервер**

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

6. **Откройте дашборд**

Перейдите в браузере по адресу `http://localhost:8000/dashboard/` .

7. **Альтернатива через Docker**

```bash
docker-compose -f docker/docker-compose.yml up --build
```

***

Если хочешь, могу следующим шагом написать билингвальный `CONTRIBUTING.md` или `docs/architecture.md` для Angel‑in‑Pocket 2.0, уже с описанием слоёв ангела, науки, искусства и бизнеса.