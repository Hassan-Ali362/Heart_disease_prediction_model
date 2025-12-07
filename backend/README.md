# Credit Card Fraud Detection Backend

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python main.py
```

Or use uvicorn directly:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Connecting Your Google Colab Model

### Option 1: Download and Load Model File
1. In Colab, save your trained model:
```python
import joblib
joblib.dump(model, 'fraud_model.pkl')
```

2. Download the file and place it in the `backend` folder

3. Update `main.py` to load the model:
```python
import joblib
model = joblib.load('fraud_model.pkl')
```

### Option 2: Use Colab as API (via ngrok)
1. In your Colab notebook, expose an API endpoint using ngrok
2. Update the `COLAB_API_URL` in `main.py`
3. Make requests to your Colab endpoint

## API Endpoints

- `GET /` - Health check
- `POST /predict` - Predict fraud
  - Body: `{"amount": 100.0, "v1": 1.5, "v2": -2.3, "v3": 0.8}`
  - Response: `{"fraud": false, "confidence": 0.85, "message": "..."}`
