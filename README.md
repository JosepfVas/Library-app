## REST API для управления библиотекой.

### API предоставляет возможность для управления книгами, авторами и пользователями, а также отслеживает выдачу книг пользователям.

## Инструкция по запуску:

### Клонирование репозитория

Для начала клонируйте репозиторий:

```
git clone https://github.com/JosepfVas/Library-app.git
```

Установка и настройка
Для установки проекта локально выполните следующие шаги:

1. Переход в директорию проекта и создание виртуального окружения
   Перейдите в директорию проекта и создайте виртуальное окружение:

```
cd Library-app
```

```
python -m venv venv
```

2. Активация виртуального окружения
   Активируйте виртуальное окружение:
   На Windows:

```
venv\Scripts\activate
```

На Unix или MacOS:

```
source venv/bin/activate
```

3. Установка зависимостей с помощью pip:

```
pip install -r requirements.txt
```

4. Установка зависимостей с помощью Poetry:

```
poetry install
```

5. Настройка переменных окружения
   Создайте файл .env по образцу .env.sample и заполните необходимыми значениями.

6. Выполнение миграций базы данных
   Выполните миграции:

```
python manage.py migrate
```

7. Запуск сервера разработки

```
python manage.py runserver
```

8. Запуск с помощью Docker
   Для запуска проекта с использованием Docker выполните следующую команду:

```
docker-compose up -d --build
```

Теперь проект должен быть успешно установлен и запущен.
