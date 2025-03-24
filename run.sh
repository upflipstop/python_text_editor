#!/bin/bash

# Добавляем обработку ошибок
set -e

# Проверка версии Python
REQUIRED_PYTHON_VERSION="3.8"
CURRENT_PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')

if [ "$(printf '%s\n' "$REQUIRED_PYTHON_VERSION" "$CURRENT_PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_PYTHON_VERSION" ]; then 
    echo "Требуется Python версии $REQUIRED_PYTHON_VERSION или выше"
    exit 1
fi

# Проверка наличия папки venv
if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..."
    
    # Создание виртуального окружения с указанием конкретной версии Python
    python3 -m venv venv || {
        echo "Ошибка при создании виртуального окружения"
        exit 1
    }
    
    echo "Виртуальное окружение создано успешно"
fi

# Активация виртуального окружения
source venv/bin/activate || {
    echo "Ошибка при активации виртуального окружения"
    exit 1
}

# Обновление pip
python -m pip install --upgrade pip

# Установка зависимостей
if [ -f "requirements.txt" ]; then
    echo "Установка зависимостей..."
    pip install -r requirements.txt || {
        echo "Ошибка при установке зависимостей"
        exit 1
    }
    
    # Установка дополнительных зависимостей для тестирования
    pip install pytest pytest-cov pytest-qt || {
        echo "Ошибка при установке зависимостей для тестирования"
        exit 1
    }
else
    echo "ОШИБКА: Файл 'requirements.txt' не найден"
    exit 1
fi

# Проверка наличия основного файла
if [ ! -f "main.py" ]; then
    echo "ОШИБКА: Файл 'main.py' не найден"
    exit 1
fi

# Запуск тестов с покрытием
echo "Запуск тестов..."
python -m pytest --cov=src tests/ --cov-report=html || {
    echo "Ошибка при выполнении тестов"
    exit 1
}

# Запуск проекта
echo "Запуск приложения..."
python main.py

# Деактивация виртуального окружения
deactivate
