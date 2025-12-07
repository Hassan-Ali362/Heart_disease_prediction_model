import axios from "axios";

const API = axios.create({
  // Change this to your backend URL:
  // - Local: http://localhost:8000
  // - ngrok: https://your-ngrok-url.ngrok-free.app
  // - Railway: https://your-app.railway.app
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});

export default API;
