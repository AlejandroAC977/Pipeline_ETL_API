# 🌦️ Weather ETL Pipeline

## 📌 Descripción

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) en Python que obtiene datos meteorológicos desde una API externa, los procesa y los almacena en formato CSV para su posterior análisis.

## ⚙️ Funcionamiento

El flujo del proyecto se divide en tres etapas principales:

* **Extract:** Se consumen datos de una API de clima utilizando solicitudes HTTP.
* **Transform:** Se limpian y estructuran los datos relevantes en un formato tabular utilizando pandas.
* **Load:** Los datos procesados se almacenan en archivos CSV dentro del proyecto.

## 🧰 Tecnologías utilizadas

* Python
* pandas
* requests
* python-dotenv

## 🔐 Seguridad

Las credenciales sensibles (como la API key) se manejan mediante variables de entorno utilizando un archivo `.env`, evitando su exposición en el repositorio.

## 📂 Estructura del proyecto

* `src/`: Código fuente del pipeline
* `data/`: Archivos generados (no incluidos en el repositorio)
* `requirements.txt`: Dependencias del proyecto

## 🚀 Uso

1. Clonar el repositorio
2. Instalar dependencias con `pip install -r requirements.txt`
3. Crear un archivo `.env` con la API key
4. Ejecutar el pipeline desde `main.py`

## 🎯 Objetivo

Demostrar la implementación de un flujo ETL básico aplicando buenas prácticas de desarrollo, manejo de datos y seguridad.

