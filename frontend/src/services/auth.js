import axios from "axios";

const api = axios.create({
  baseURL: "/api/v1", // Proxifié vers http://backend:8000/api/v1
});

// Ajouter le token dynamiquement
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export const loginUser = async (email, password) => {
  try {
    const response = await api.post("/user/login", { email, password });
    const { token } = response.data;
    localStorage.setItem("token", token); // Stocker le token
    return response.data;
  } catch (error) {
    console.error("Login error:", error.response?.data || error.message);
    throw error;
  }
};
