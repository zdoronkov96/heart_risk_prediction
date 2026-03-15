import joblib
import pandas as pd
from fastapi import FastAPI, UploadFile, File
import io
import re

app = FastAPI()

# Загружаем модель
model = joblib.load("model.pkl")

EXPECTED_COLUMNS = [
    'age', 'cholesterol', 'heart_rate', 'diabetes', 'family_history',
    'smoking', 'obesity', 'alcohol_consumption', 'diet',
    'previous_heart_problems', 'medication_use', 'stress_level', 'income',
    'bmi', 'triglycerides', 'physical_activity_days_per_week',
    'blood_sugar', 'ckmb', 'troponin', 'gender', 'systolic_blood_pressure',
    'diastolic_blood_pressure'
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # 1. Читаем CSV файл
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
    
    # 2. Простая предобработка
    # Удаляем лишние колонки
    cols_to_drop = ['Unnamed: 0', 'sedentary_hours_per_day', 
                   'exercise_hours_per_week', 'sleep_hours_per_day']
    for col in cols_to_drop:
        if col in df.columns:
            df = df.drop(col, axis=1)
    
    # Приводим названия колонок к нижнему регистру
    new_columns = []
    for col in df.columns:
        col = str(col).lower()
        col = col.replace(' ', '_')
        col = re.sub(r"[-()]", '', col)
        new_columns.append(col)
    df.columns = new_columns
    
    # Проверяем наличие всех нужных колонок
    missing_cols = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing_cols:
        return {"error": f"Отсутствуют колонки: {missing_cols}"}
    
    # Упорядочиваем колонки
    df = df[EXPECTED_COLUMNS]
    
    # 3. Делаем предсказания
    predictions = model.predict(df)
    
    # 4. Формируем ответ
    results = []
    for i, pred in enumerate(predictions):
        results.append({
            "id": i,
            "prediction": int(pred),
            "risk": "High" if pred == 1 else "Low"
        })
    
    return {
        "filename": file.filename,
        "total": len(results),
        "high_risk": int(sum(predictions)),
        "low_risk": int(len(predictions) - sum(predictions)),
        "results": results
    }