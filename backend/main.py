from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import os

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PatientData(BaseModel):
    age: int
    sex: int  # 1 = male, 0 = female
    cp: int  # chest pain type (0-3)
    trestbps: int  # resting blood pressure
    chol: int  # serum cholesterol in mg/dl
    fbs: int  # fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
    restecg: int  # resting electrocardiographic results (0-2)
    thalach: int  # maximum heart rate achieved
    exang: int  # exercise induced angina (1 = yes, 0 = no)
    oldpeak: float  # ST depression induced by exercise
    slope: int  # slope of peak exercise ST segment (0-2)
    ca: int  # number of major vessels colored by fluoroscopy (0-4)
    thal: int  # thalassemia (0-3)

# ============================================
# MODEL LOADING - REPLACE WITH YOUR MODEL
# ============================================

# Load your downloaded Colab model
from model_loader import ModelLoader

# Try to load the model (will use dummy prediction if not found)
# Change filename to match your heart disease model
model_loader = ModelLoader('hear_disease_model.pkl')

@app.get("/")
def read_root():
    return {
        "message": "Heart Disease Prediction API",
        "model_loaded": model_loader is not None and model_loader.is_loaded() if model_loader else False
    }

@app.post("/predict")
def predict_heart_disease(data: PatientData):
    # Prepare input features in correct order
    features = [
        data.age,
        data.sex,
        data.cp,
        data.trestbps,
        data.chol,
        data.fbs,
        data.restecg,
        data.thalach,
        data.exang,
        data.oldpeak,
        data.slope,
        data.ca,
        data.thal
    ]
    
    # ============================================
    # REAL MODEL PREDICTION
    # ============================================
    
    if model_loader and model_loader.is_loaded():
        try:
            result = model_loader.predict(features)
            return {
                "disease": bool(result['prediction']),
                "confidence": result['confidence'],
                "message": "⚠️ Heart disease detected. Please consult a doctor." if result['prediction'] else "✅ No heart disease detected. Stay healthy!"
            }
        except Exception as e:
            return {
                "disease": False,
                "confidence": 0.0,
                "message": f"⚠️ Prediction error: {str(e)}"
            }
    
    # ============================================
    # FALLBACK: If model not loaded, use dummy prediction
    # ============================================
    # Simple rule: high risk if age > 60 and high cholesterol
    prediction = 1 if (data.age > 60 and data.chol > 240) else 0
    
    return {
        "disease": bool(prediction),
        "confidence": 0.85,
        "message": "⚠️ Model not found. Using dummy prediction."
    }

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("❤️  Starting Heart Disease Prediction API")
    print("="*60)
    if model_loader and model_loader.is_loaded():
        print("✅ Model loaded successfully!")
    else:
        print("⚠️  No model loaded - using dummy predictions")
        print("📝 To load your model:")
        print("   1. Place heart_model.pkl in backend folder")
        print("   2. Model will load automatically")
        print("   3. Restart the server")
    print("="*60)
    print("🌐 API running at: http://localhost:8000")
    print("📖 Docs available at: http://localhost:8000/docs")
    print("="*60 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
