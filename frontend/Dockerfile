# Instalando en base a la imagen de node
FROM node:iron-slim

# Paso 2: Crear una carpeta de trabajo
WORKDIR /app

# Paso 3: Copiar los listados de dependencias e instalarlas
COPY package*.json ./
RUN npm install

# Paso 4: Copiar el resto del código
COPY . .

# Paso 5: El comando para encender el servicio
CMD ["npm", "start"]