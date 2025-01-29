# Dockerfile
FROM python:3.9-slim
 
WORKDIR /app
 
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el script SQL a la carpeta de inicialización
COPY ./init.sql /docker-entrypoint-initdb.d/init.sql
 
# Verifica que el script tenga los permisos correctos
RUN chmod +x /docker-entrypoint-initdb.d/init.sql

COPY . .
 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]