
# Цель проекта
Разработать приложение для предсказания риска сердечного приступа

# Задачи проекта
* Построить модель машинного обучения, которая на основе представленной характерисии пациента предсказывает категориальный показательный риска сердечного приступа  — высокий или низкий
* Сделать приложение для получения предсказаний сердечного приступа по пользовательскому запросу.

# Исходные данные
Данные взяты из следующих файлов:
* heart_train.csv
* heart_test.csv

Обозначение столбцов:


* **id** - уникальный номер пациента
* **Age** - возраст пациента в годах
* **Cholesterol** - уровень холестерина в крови
* **Heart rate** - уровень пульса
* **Diabetes** - наличие сахарного диабета 
* **Family History** - наличия сердечно-сосудистых заболеваний у близких родственников пациента
* **Smoking** - курит ли пациент
* **Obesity** - наличие ожирения
* **Alcohol Consumption** - потребляет ли алкоголь
* **Exercise Hours Per Week** - сколько часов упражняется в неделю
* **Diet** - тип диеты
* **Previous Heart Problems** - наличие проблем с сердцем в прошлом
* **Medication Use** - принимает ли пациент лекарственные препараты
* **Stress Level** - уровень стресса
* **Sedentary Hours Per Day** - сколько часов сидит в день
* **Income** - доход пациента
* **BMI** - индекс массы тела
* **Triglycerides** - уровень триглицеридов в крови
* **Physical Activity Days Per Week** - сколько раз в неделю пациент занимается физической активностью 
* **Sleep Hours Per Day** - сколько часов в день пациент спит
* **Heart Attack Risk (Binary)** - риск инфаркта **(целевой признак)**
* **Blood sugar** - уровень сахара
* **CK-MB** - уровень креатинкиназа-MB
* **Troponin** - уровень тропонина
* **Gender** - пол
* **Systolic blood pressure** - систолическое давление 
* **Diastolic blood pressure** - диастолическое давление

# Библиотеки

* numpy
* pandas
* matplotlib.pyplot
* seaborn
* shap
* IPython.display
* re
* catboost
* sklearn.model_selection
* sklearn.metrics
* json
* joblib
* phik

# КРАТКАЯ ИНСТРУКЦИЯ ПО ЗАПУСКУ ПРИЛОЖЕНИЯ

## 1. Установка
### Клонируем репозиторий
git clone https://github.com/zdoronkov96/heart_risk_prediction.git
cd heart_risk_prediction

### Устанавливаем зависимости
pip install fastapi uvicorn pandas joblib python-multipart

## 2. Запуск сервера
uvicorn main_api:app --reload
Сервер запустится по адресу: http://localhost:8000


## 3. Использование API через браузер (Swagger UI)
    Откройте http://localhost:8000/docs
    
    Нажмите на эндпоинт /predict
    
    Кнопка "Try it out" → выберите CSV файл → "Execute"
    
    Получите JSON с предсказаниями
