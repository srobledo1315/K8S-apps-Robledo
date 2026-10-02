FROM python:3.9-slim

WORKDIR /app

# Crear usuario sin privilegios para mitigar escalada de privilegios
RUN useradd -u 10001 -m appuser

# Copiar e instalar dependencias con caché optimizado
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app.py /app/

# Usar usuario no root
USER 10001

EXPOSE 5000

CMD ["python", "app.py"]
