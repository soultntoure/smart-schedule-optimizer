# Multi-stage build for backend
FROM python:3.9-slim-buster as backend-builder
WORKDIR /app/backend
COPY ./backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./backend/ .

FROM python:3.9-slim-buster as backend-runner
WORKDIR /app/backend
COPY --from=backend-builder /app/backend /app/backend
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Multi-stage build for frontend
FROM node:18-alpine as frontend-builder
WORKDIR /app/frontend
COPY ./frontend/package.json ./frontend/package-lock.json .
RUN npm install
COPY ./frontend/ .
RUN npm run build

FROM nginx:stable-alpine as frontend-runner
COPY --from=frontend-builder /app/frontend/build /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
