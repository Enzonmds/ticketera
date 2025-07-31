# Ticketera

[![CI/CD to Staging](https://github.com/Enzonmds/ticketera/actions/workflows/deploy-staging.yml/badge.svg)](https://github.com/Enzonmds/ticketera/actions)

"Sistema de Gestión de Tickets para equipos de soporte, construido con Django y React.

## 🚀 Tecnologías Utilizadas

Este proyecto utiliza un stack de tecnologías moderno y escalable:

* **Backend**:
    * **Django**: Framework principal de Python para el desarrollo del backend.
    * **Django REST Framework**: Para la creación de la API REST.
    * **Celery**: Para la gestión de tareas asíncronas (ej: envío de correos).
    * **Redis**: Como message broker para Celery y para caché.
* **Frontend**:
    * **React**: Biblioteca de JavaScript para construir la interfaz de usuario.
* **Base de Datos**:
    * **PostgreSQL**: Alojada en **Neon.tech** (Serverless Postgres).
* **Contenerización**:
    * **Docker & Docker Compose**: Para crear un entorno de desarrollo consistente y para el despliegue.
* **Infraestructura y Despliegue (CI/CD)**:
    * **Google Cloud Platform (GCP)**: La Máquina Virtual (VM) para el entorno de Staging.
    * **GitHub Actions**: Para la integración y despliegue continuo automatizado.

## 🛠️ Instalación y Puesta en Marcha Local

Para levantar el proyecto en tu máquina local, necesitás tener **Docker** y **Docker Compose** instalados.

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Enzonmds/ticketera.git](https://github.com/Enzonmds/ticketera.git)
    cd ticketera
    ```

2.  **Configurar las variables de entorno:**
    * Crea una copia del archivo de ejemplo `.env.example` y renómbrala a `.env`.
        ```bash
        cp .env.example .env
        ```
    * Abre el archivo `.env` y rellena las variables con tus credenciales locales de desarrollo para PostgreSQL, Redis, etc.

3.  **Levantar los servicios con Docker Compose:**
    Este único comando construirá las imágenes y levantará todos los contenedores (backend, base de datos y redis).
    ```bash
    docker compose up --build
    ```

## ⚙️ Uso

Una vez que los contenedores estén corriendo, podrás acceder a:

* **API del Backend (Django)**: `http://localhost:8000/api/`
* **Aplicación Frontend (React)**: `http://localhost:3000`

## 🌿 Estrategia de Ramas (Branching Strategy)

Este repositorio utiliza un flujo de trabajo basado en **Git Flow Lite**:

* `main`: Contiene el código en producción. Es la rama más estable.
* `develop`: Es la rama de integración. Todo el trabajo nuevo se mezcla aquí primero y se despliega automáticamente a **Staging**.
* `feature/<nombre-feature>`: Todas las nuevas funcionalidades o correcciones se desarrollan en su propia rama, que sale de `develop` y vuelve a `develop` a través de un Pull Request.

## 🔄 Pipeline de CI/CD

El proyecto está configurado con un pipeline de Integración y Despliegue Continuo usando **GitHub Actions**.

* Cada `push` a la rama `develop` dispara automáticamente un workflow que:
    1.  Se conecta al servidor de **Staging** en GCP.
    2.  Descarga los últimos cambios.
    3.  Reconstruye y reinicia los contenedores de Docker.

Esto asegura que el entorno de Staging siempre refleje la última versión de la rama `develop`.