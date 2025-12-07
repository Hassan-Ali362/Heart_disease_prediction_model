"""
Helper functions to integrate with Google Colab model
"""
import requests
import numpy as np

class ColabModelClient:
    """Client to communicate with Google Colab model via ngrok"""
    
    def __init__(self, colab_url):
        self.colab_url = colab_url.rstrip('/')
    
    def predict(self, features):
        """
        Send prediction request to Colab endpoint
        
        Args:
            features: numpy array or list of features
            
        Returns:
            prediction result
        """
        try:
            response = requests.post(
                f"{self.colab_url}/predict",
                json={"features": features.tolist() if isinstance(features, np.ndarray) else features},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"Error calling Colab API: {str(e)}")

# Example usage in main.py:
# from colab_integration import ColabModelClient
# colab_client = ColabModelClient("https://your-ngrok-url.ngrok.io")
# result = colab_client.predict(features)
