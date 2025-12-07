import axios from "axios";

const API = axios.create({
  baseURL: "http://0.0.0.0:8000",
});

export default API;
