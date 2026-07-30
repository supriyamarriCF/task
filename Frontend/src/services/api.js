import axios from "axios";

const api = axios.create({
  baseURL: "https://task-2-hjlr.onrender.com",
});

export const getStudents = async () => {
  const response = await api.get("/students");
  return response.data;
};

export const createStudent = async (student) => {
  const response = await api.post("/students", student);
  return response.data;
};

export default api;