"""
Model Loader for Google Colab Models
Supports loading models from .pkl, .h5, .joblib files
"""
import os
import numpy as np

class ModelLoader:
    def __init__(self, model_path=None):
        self.model = None
        self.model_type = None
        
        if model_path and os.path.exists(model_path):
            self.load_model(model_path)
    
    def load_model(self, model_path):
        """Load model from file"""
        try:
            # Try joblib first (sklearn models)
            if model_path.endswith('.pkl') or model_path.endswith('.joblib'):
                import joblib
                self.model = joblib.load(model_path)
                self.model_type = 'sklearn'
                print(f"✅ Loaded sklearn model from {model_path}")
                return True
            
            # Try pickle
            elif model_path.endswith('.pickle'):
                import pickle
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)
                self.model_type = 'sklearn'
                print(f"✅ Loaded pickle model from {model_path}")
                return True
            
            # Try Keras/TensorFlow
            elif model_path.endswith('.h5') or model_path.endswith('.keras'):
                from tensorflow import keras
                self.model = keras.models.load_model(model_path)
                self.model_type = 'keras'
                print(f"✅ Loaded Keras model from {model_path}")
                return True
            
            else:
                print(f"❌ Unsupported model format: {model_path}")
                return False
                
        except Exception as e:
            print(f"❌ Error loading model: {str(e)}")
            return False
    
    def predict(self, features):
        """Make prediction with loaded model"""
        if self.model is None:
            raise Exception("No model loaded. Please load a model first.")
        
        try:
            # Convert to numpy array if needed
            if not isinstance(features, np.ndarray):
                features = np.array(features)
            
            # Ensure 2D array
            if len(features.shape) == 1:
                features = features.reshape(1, -1)
            
            # Make prediction based on model type
            if self.model_type == 'sklearn':
                prediction = self.model.predict(features)[0]
                
                # Try to get probability if available
                try:
                    proba = self.model.predict_proba(features)[0]
                    confidence = float(max(proba))
                except:
                    confidence = 0.85  # Default confidence
                
                return {
                    'prediction': int(prediction),
                    'confidence': confidence
                }
            
            elif self.model_type == 'keras':
                prediction = self.model.predict(features, verbose=0)[0]
                
                # For binary classification
                if len(prediction) == 1:
                    confidence = float(prediction[0])
                    pred_class = 1 if confidence > 0.5 else 0
                else:
                    pred_class = int(np.argmax(prediction))
                    confidence = float(max(prediction))
                
                return {
                    'prediction': pred_class,
                    'confidence': confidence
                }
            
        except Exception as e:
            raise Exception(f"Prediction error: {str(e)}")
    
    def is_loaded(self):
        """Check if model is loaded"""
        return self.model is not None

# Example usage:
# loader = ModelLoader('fraud_model.pkl')
# result = loader.predict([100.0, 1.5, -2.3, 0.8])
# print(result)  # {'prediction': 0, 'confidence': 0.95}
