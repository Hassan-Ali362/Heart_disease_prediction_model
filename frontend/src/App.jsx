import { useState, useEffect } from "react";
import API from "./Api";
import "./App.css";

function App() {
  // Sample patient data with default values
  const [form, setForm] = useState({
    age: "45",
    sex: "1",
    cp: "0",
    trestbps: "120",
    chol: "200",
    fbs: "0",
    restecg: "0",
    thalach: "150",
    exang: "0",
    oldpeak: "0.0",
    slope: "0",
    ca: "0",
    thal: "2"
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Request notification permission on mount
  useEffect(() => {
    if ("Notification" in window && Notification.permission === "default") {
      Notification.requestPermission();
    }
  }, []);

  const showNotification = (title, body, isDisease) => {
    if ("Notification" in window && Notification.permission === "granted") {
      new Notification(title, {
        body: body,
        icon: isDisease ? "🚨" : "✅",
        badge: isDisease ? "⚠️" : "✅",
        tag: "heart-disease-prediction",
        requireInteraction: isDisease, // Keep notification visible if disease detected
      });
    }
  };

  const getSuggestions = (data) => {
    if (data.disease) {
      return {
        title: "⚠️ Heart Disease Risk Detected",
        suggestions: [
          "🏥 Consult a cardiologist immediately for proper diagnosis",
          "💊 Follow prescribed medications and treatment plans",
          "🏃 Start light exercise after doctor's approval",
          "🥗 Adopt a heart-healthy diet (low sodium, low fat)",
          "🚭 Quit smoking and limit alcohol consumption",
          "😌 Manage stress through meditation or yoga",
          "📊 Monitor blood pressure and cholesterol regularly",
          "⚖️ Maintain a healthy weight",
          "💤 Get adequate sleep (7-8 hours daily)"
        ],
        urgency: "high"
      };
    } else {
      return {
        title: "✅ No Heart Disease Detected",
        suggestions: [
          "🎉 Great news! Your heart appears healthy",
          "🏃 Continue regular physical activity (30 min/day)",
          "🥗 Maintain a balanced, nutritious diet",
          "💧 Stay hydrated (8 glasses of water daily)",
          "😊 Keep stress levels low",
          "🚭 Avoid smoking and excessive alcohol",
          "📅 Schedule regular health checkups",
          "💪 Maintain a healthy weight",
          "😴 Get quality sleep consistently"
        ],
        urgency: "low"
      };
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      // Convert values to appropriate types
      const payload = {
        age: parseInt(form.age),
        sex: parseInt(form.sex),
        cp: parseInt(form.cp),
        trestbps: parseInt(form.trestbps),
        chol: parseInt(form.chol),
        fbs: parseInt(form.fbs),
        restecg: parseInt(form.restecg),
        thalach: parseInt(form.thalach),
        exang: parseInt(form.exang),
        oldpeak: parseFloat(form.oldpeak),
        slope: parseInt(form.slope),
        ca: parseInt(form.ca),
        thal: parseInt(form.thal)
      };
      
      const res = await API.post("/predict", payload);
      const resultData = res.data;
      setResult(resultData);

      // Show browser notification
      const notificationTitle = resultData.disease 
        ? "⚠️ Heart Disease Detected" 
        : "✅ No Heart Disease";
      const notificationBody = resultData.message;
      showNotification(notificationTitle, notificationBody, resultData.disease);

      // Scroll to result
      setTimeout(() => {
        document.querySelector('.result')?.scrollIntoView({ 
          behavior: 'smooth', 
          block: 'nearest' 
        });
      }, 100);

    } catch (err) {
      setError("Failed to connect to backend. Make sure it's running on port 8000.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1 className="main-title">❤️ Heart Disease Prediction</h1>
      <p className="main-subtitle">Enter patient information to predict heart disease risk</p>
      
      <div className="two-column-layout">
        {/* Left Column - Input Form */}
        <div className="card input-card">
          <h2 className="card-title">Patient Information</h2>
          
          <form onSubmit={handleSubmit}>
          <div className="form-scroll">
            <div className="form-group">
              <label>Age (years)</label>
              <input 
                type="number" 
                name="age" 
                value={form.age}
                onChange={handleChange}
                min="1"
                max="120"
                required 
              />
            </div>

            <div className="form-group">
              <label>Sex</label>
              <select 
                name="sex" 
                value={form.sex}
                onChange={handleChange}
                required
              >
                <option value="1">Male</option>
                <option value="0">Female</option>
              </select>
            </div>

            <div className="form-group">
              <label>Chest Pain Type</label>
              <select 
                name="cp" 
                value={form.cp}
                onChange={handleChange}
                required
              >
                <option value="0">Typical Angina</option>
                <option value="1">Atypical Angina</option>
                <option value="2">Non-anginal Pain</option>
                <option value="3">Asymptomatic</option>
              </select>
            </div>

            <div className="form-group">
              <label>Resting Blood Pressure (mm Hg)</label>
              <input 
                type="number" 
                name="trestbps" 
                value={form.trestbps}
                onChange={handleChange}
                min="80"
                max="200"
                required 
              />
            </div>

            <div className="form-group">
              <label>Cholesterol (mg/dl)</label>
              <input 
                type="number" 
                name="chol" 
                value={form.chol}
                onChange={handleChange}
                min="100"
                max="600"
                required 
              />
            </div>

            <div className="form-group">
              <label>Fasting Blood Sugar &gt; 120 mg/dl</label>
              <select 
                name="fbs" 
                value={form.fbs}
                onChange={handleChange}
                required
              >
                <option value="0">No</option>
                <option value="1">Yes</option>
              </select>
            </div>

            <div className="form-group">
              <label>Resting ECG Results</label>
              <select 
                name="restecg" 
                value={form.restecg}
                onChange={handleChange}
                required
              >
                <option value="0">Normal</option>
                <option value="1">ST-T Wave Abnormality</option>
                <option value="2">Left Ventricular Hypertrophy</option>
              </select>
            </div>

            <div className="form-group">
              <label>Maximum Heart Rate Achieved</label>
              <input 
                type="number" 
                name="thalach" 
                value={form.thalach}
                onChange={handleChange}
                min="60"
                max="220"
                required 
              />
            </div>

            <div className="form-group">
              <label>Exercise Induced Angina</label>
              <select 
                name="exang" 
                value={form.exang}
                onChange={handleChange}
                required
              >
                <option value="0">No</option>
                <option value="1">Yes</option>
              </select>
            </div>

            <div className="form-group">
              <label>ST Depression (oldpeak)</label>
              <input 
                type="number" 
                step="0.1"
                name="oldpeak" 
                value={form.oldpeak}
                onChange={handleChange}
                min="0"
                max="10"
                required 
              />
            </div>

            <div className="form-group">
              <label>Slope of Peak Exercise ST Segment</label>
              <select 
                name="slope" 
                value={form.slope}
                onChange={handleChange}
                required
              >
                <option value="0">Upsloping</option>
                <option value="1">Flat</option>
                <option value="2">Downsloping</option>
              </select>
            </div>

            <div className="form-group">
              <label>Number of Major Vessels (0-4)</label>
              <select 
                name="ca" 
                value={form.ca}
                onChange={handleChange}
                required
              >
                <option value="0">0</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
              </select>
            </div>

            <div className="form-group">
              <label>Thalassemia</label>
              <select 
                name="thal" 
                value={form.thal}
                onChange={handleChange}
                required
              >
                <option value="0">Normal</option>
                <option value="1">Fixed Defect</option>
                <option value="2">Reversible Defect</option>
                <option value="3">Not Described</option>
              </select>
            </div>
          </div>

            <button type="submit" disabled={loading}>
              {loading ? "Analyzing..." : "Predict Heart Disease"}
            </button>
          </form>
        </div>

        {/* Right Column - Results */}
        <div className="card result-card">
          {!result && !error && !loading && (
            <div className="placeholder">
              <div className="placeholder-icon">📊</div>
              <h3>Prediction Results</h3>
              <p>Fill in the patient information and click "Predict Heart Disease" to see results here.</p>
            </div>
          )}

          {loading && (
            <div className="placeholder">
              <div className="loader"></div>
              <h3>Analyzing...</h3>
              <p>Processing patient data...</p>
            </div>
          )}

          {error && (
            <div className="result error">
              <p>⚠️ {error}</p>
            </div>
          )}

          {result && !error && (
            <div className={`result ${result.disease ? "fraud" : "safe"}`}>
            <h2>{result.disease ? "⚠️ HEART DISEASE DETECTED" : "✅ NO HEART DISEASE"}</h2>
            <p>{result.message}</p>
            {result.confidence && (
              <p style={{marginTop: '12px', fontSize: '18px', fontWeight: '600'}}>
                Confidence: {(result.confidence * 100).toFixed(1)}%
              </p>
            )}
            
            {/* Suggestions Section */}
            <div className="suggestions">
              <h3>{getSuggestions(result).title}</h3>
              <ul>
                {getSuggestions(result).suggestions.map((suggestion, index) => (
                  <li key={index}>{suggestion}</li>
                ))}
              </ul>
            </div>
          </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
