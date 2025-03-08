import axios from "axios";

const api = axios.create({
  baseURL: "/api/v1", // Chemin relatif, proxifié par package.json
});

// Intercepteur pour ajouter le token dynamiquement
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

export const fetchDeclarations = () => api.get("/tax/").then((res) => res.data);

export const uploadDeclarations = (formData) =>
  api.post("/tax/upload", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

export const createDeclaration = (data) => api.post("/tax/", data);

/*export const loginUser = (email, password) =>
  api
    .post("/user/login", { email, password })
    .then((res) => {
      const { token } = res.data; // Supposant que le backend renvoie {"token": "..."}
      localStorage.setItem("token", token); // Stocker le token
      return res.data;
    })
    .catch((error) => {
      console.error("Login error:", error.response?.data || error.message);
      throw error;
    });*/
