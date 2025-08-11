# 🧪 Entorno de Pruebas Automatizadas con Selenium + Docker

Este proyecto configura un entorno completo de pruebas automatizadas usando **Selenium Grid**, **Docker**, **Flask**, **Pytest**, y herramientas de monitoreo como **Prometheus**, **Grafana** y **Portainer**. Simula un formulario de inicio de sesión y lo valida mediante automatización de navegador, todo dentro de contenedores aislados.

---

## 📦 Estructura del Proyecto

selenium/ 

├── .github/ 
│     └── workflows/ 
│       └── ci.yml 

├── app/ 
│   ├── app.py 
│   ├── dockerfile 
│   └── requirements.txt 

├── test/ 
│   ├── test_login.py 
│   ├── dockerfile 
│   └── requirements.txt 

├── monitoring/ 
│   └── prometheus.yml 

├── docker-compose.yml


---

## 🚀 Descripción de Componentes

### 🔧 `app/` — Simulación de Login con Flask
- Formulario simple con credenciales fijas (`user` / `pass`)
- Valida entrada y muestra `"Bienvenido"` al éxito
- Corre en `0.0.0.0:5000`

### 🧪 `test/` — Selenium + Pytest
- Se conecta al Selenium Hub vía `SELENIUM_REMOTE_URL`
- Automatiza interacción con el formulario
- Valida presencia de `"Bienvenido"` en la respuesta
- Contenerizado con su propio `Dockerfile` y dependencias

### 🐳 `docker-compose.yml` — Orquestación
Incluye:
- `selenium-hub` + nodo `chrome`
- Contenedor `app`
- Contenedor `tests`
- `prometheus`, `grafana`, `n8n`, `portainer`
- Red compartida: `selenium-net`
- Volúmenes persistentes para monitoreo y gestión

### 📊 Monitoreo
- `prometheus.yml` recolecta métricas de Prometheus
- Grafana y Portainer ofrecen dashboards y gestión visual

---

## ⚙️ Pipeline CI/CD (`.github/workflows/ci.yml`)

Se ejecuta al hacer push o pull request a `main`:
1. Clona el código
2. Configura Docker Buildx
3. Levanta servicios con `docker-compose`
4. Espera inicialización
5. Ejecuta pruebas en el contenedor `tests`
6. Apaga y limpia el entorno

---

## 🛠️ Instalación y Uso

### Requisitos
- Docker y Docker Compose
- Cuenta en GitHub (para CI/CD)


# Problema
Queremos automatizar pruebas de una aplicación web para validar que funciona correctamente, y hacer todo esto usando herramientas modernas.
## Objetivo
Crear una Prueba de Concepto que incluya:
- Automatización de pruebas con Selenium.
- Empaquetado con Docker y Docker Compose.
- Integración continua con GitHub Actions.
- Monitoreo con Prometheus y Grafana.
- Administración con Portainer.
- Automatización con n8n e integración con OpenAI para análisis inteligente.

## Plan de trabajo
1. Planificar: Crear tareas (issues) y documentar el proyecto.
2. Desarrollar: Escribir los scripts de automatización y configuraciones.
3. Integrar: Automatizar pruebas y despliegues con GitHub Actions.
4. Probar: Validar el funcionamiento con pruebas automatizadas.
5. Lanzar: Desplegar con Docker y Docker Compose.
6. Operar: Administrar contenedores con Portainer.
7. Observar: Monitorear logs y métricas con Prometheus y Grafana.
8. IA integrada: Analizar logs y automatizar tareas con n8n y OpenAI.

## Estructura del proyecto
- `/app`: Código de la aplicación web.
- `/test`: Pruebas automatizadas con Selenium.
- `/monitoring`: Configuración de Prometheus.
- `docker-compose.yml`: Definición de los contenedores Docker.
- `.github/workflows/ci.yml`: Pipeline de CI con GitHub Actions.



