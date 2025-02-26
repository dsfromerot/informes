# Usar una imagen base de Python ligera
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar las dependencias sin caché para reducir el tamaño de la imagen
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto
COPY . .

# Configurar PYTHONPATH para evitar problemas de importación
ENV PYTHONPATH=/app

# Exponer el puerto en el que corre la aplicación
EXPOSE 5003

# Comando para ejecutar la aplicación
RUN pip install gunicorn
CMD gunicorn --bind 0.0.0.0:5003 "app.config:start()"
