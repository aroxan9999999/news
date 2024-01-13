# Используем официальный образ Python 3.9 как базовый
FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app

# Установка переменных окружения для Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "--workers", "3", "--bind", "localhost:8000", "news.wsgi:application"]
