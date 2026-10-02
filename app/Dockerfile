FROM python:3.9-slim

WORKDIR /app

# Usuario de sistema sin privilegios
RUN useradd -u 10001 -m appuser

# Instalación de dependencias fijadas
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar arquitectura limpia y entrypoint
COPY src/ /app/src/
COPY app.py /app/

USER 10001
EXPOSE 5000

CMD ["python", "app.py"]
