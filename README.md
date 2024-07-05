# 📁 Reservations

## 📖 Кратко о проекте

Учебный проект для освоения FastApi. Сервис резервирования отелей, что-то похоже на 
Booking. Целью являлось освоение таких технологий как FastApi, alembic, SQLAlchemy, 
uvicorn, pydantic. 
---

## 🧾 TODO список (основные положения)

- [x] Настроить инициализацию проекта FastAPI с использованием Uvicorn для асинхронки.
- [x] Создать модели SQLAlchemy для основных сущностей приложения.
- [x] Использовать Alembic для управления миграциями базы данных.
- [x] Реализовать CRUD операции для основных сущностей приложения.
- [x] Реализовать систему бронирования номеров отеля с учетом доступных дат и цен.
- [x] Создать личный кабинет пользователя с отображением текущих бронирований и истории заказов.
- [x] Оптимизировать работу с базой данных для эффективного выполнения запросов при высоких нагрузках.
- [x] Добавить docker-compose и балансировщик нагрузок (nginx). 

---


## 💻 Запуск проекта

0. Загрузка проекта и переход в директорию 

```bash
git clone git@github.com:SamvelMhitaryan/filmapoisk.git
cd filmapoisk
```

1. Создание виртуального окружения (venv): 

```bash
python3 -m venv venv
```

2. Активация виртуального окружения (venv): 

Linux / Mac
```bash
. venv/bin/activate
```

Windows
```bash
. venv\scripts\activate
```

3. Установка зависимостей: 

```bash
pip install -r requirements.txt
```

4. Запуск: 

```bash
python3 manage.py runserver
```

# замена настроек БД и ключа django под себя.

python3 manage.py collectstatic    # \
python3 manage.py makemigrations   #  Или все одной командой через &&
python3 manage.py migrate          # /

python3 manage.py runserver 8000   # либо полноценно через gunicorn, nginx и т.д.
```