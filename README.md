Краткая инструкция по запуску приложения

# 1. Установка
# Клонируем репозиторий
git clone <ссылка-на-ваш-репозиторий>
cd <название-папки>

# Устанавливаем зависимости
pip install fastapi uvicorn pandas joblib python-multipart

# 2. Запуск сервера
uvicorn main:app --reload
Сервер запустится по адресу: http://localhost:8000


# 3. Использование API через браузер (Swagger UI)
    Откройте http://localhost:8000/docs
    
    Нажмите на эндпоинт /predict
    
    Кнопка "Try it out" → выберите CSV файл → "Execute"
    
    Получите JSON с предсказаниями
