import axios from 'axios';

const API_URL = process.env.NODE_ENV === 'production' ? '/api/v1' : 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const authApi = {
  login: (email: string, password: string) => apiClient.post('/login', { email, password }),
  register: (email: string, password: string) => apiClient.post('/users/', { email, password }),
};

export const tasksApi = {
  getTasks: () => apiClient.get('/tasks/'),
  createTask: (taskData: any) => apiClient.post('/tasks/', taskData),
};

export const schedulesApi = {
  generateSchedule: (scheduleData: any) => apiClient.post('/schedules/generate_optimized', scheduleData),
  getSchedules: () => apiClient.get('/schedules/'),
};

export const preferencesApi = {
  getPreferences: (userId: number) => apiClient.get(`/preferences/user/${userId}`),
  createPreference: (preferenceData: any) => apiClient.post('/preferences/', preferenceData),
  updatePreference: (preferenceId: number, preferenceData: any) => apiClient.put(`/preferences/${preferenceId}`, preferenceData),
};
