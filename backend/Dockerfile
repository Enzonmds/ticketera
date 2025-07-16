# Creamos a partir de la imagen de Python
FROM python:3.14.0b4-slim

# Paso 2: Crear una carpeta de trabajo dentro de la caja
WORKDIR /app

# Paso 3: Copiar solo el listado de dependencias e instalarlas
# Esto es un truco para que Docker no reinstale todo cada vez que cambiás tu código
COPY requirements.txt .
RUN pip install -r requirements.txt

# Paso 4: Copiar el resto del código de tu app a la carpeta de trabajo
COPY . .

# Paso 5: El comando que se ejecutará para encender el servicio
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]