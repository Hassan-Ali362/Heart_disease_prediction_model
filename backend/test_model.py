"""
Quick test to check if model loads correctly
"""
from model_loader import ModelLoader

print("Testing model loading...")
print("="*50)

# Try to load the model
loader = ModelLoader('fraud_model.pkl')

if loader.is_loaded():
    print("✅ Model loaded successfully!")
    print(f"   Model type: {loader.model_type}")
    
    # Test prediction
    print("\n🧪 Testing prediction...")
    test_features = [150.50, 1.5, -2.3, 0.8]
    result = loader.predict(test_features)
    
    print(f"   Input: {test_features}")
    print(f"   Prediction: {result['prediction']} (0=safe, 1=fraud)")
    print(f"   Confidence: {result['confidence']:.2%}")
    print("\n✅ Model is working correctly!")
else:
    print("❌ Model failed to load")
    print("   Make sure fraud_model.pkl is in the backend folder")

print("="*50)
