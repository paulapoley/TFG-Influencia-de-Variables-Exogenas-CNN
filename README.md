# Trabajo Fin de Grado

## Título: Influencia de Variables Exógenas en la Detección de Enfermedades de Piel mediante Redes Neuronales y Análisis de Imágenes Médicas
Este repositorio contiene el código, la documentación y los recursos relacionados con el Trabajo de Fin de Grado (TFG) sobre la detección de enfermedades cutáneas utilizando redes neuronales convolucionales (CNN) y la inclusión de variables exógenas.

## 1. Objetivo del Estudio
Este TFG investiga cómo las variables exógenas (ubicación de la lesión, edad, sexo del paciente y tipo de diagnóstico) influyen en la capacidad predictiva de los modelos de clasificación de imágenes. Se busca mejorar la precisión y eficacia en la detección de enfermedades cutáneas a través de:

- **Modelo CNN Sin Variables Exógenas:** Solo se utilizan imágenes para la detección.
- **Modelo CNN Con Variables Exógenas:** Se incorporan datos adicionales (variables exógenas) para refinar la clasificación.


## 2. Metodología
Se desarrollaron y compararon varios enfoques de detección de enfermedades cutáneas utilizando diferentes arquitecturas de CNN, tanto preentrenadas como diseñadas desde cero:

- **Modelos Preentrenados:** DenseNet121, MobileNetV2, ResNet50, EfficientNetB0, Xception.
- **Modelo Personalizado:** CNN diseñada específicamente para este estudio.

Estos modelos fueron entrenados y evaluados utilizando el conjunto de datos **Skin Cancer MNIST: HAM10000**, que contiene una gran colección de imágenes dermatoscópicas de múltiples lesiones pigmentadas, abarcando siete afecciones dermatológicas distintas.

## 3. Contenidos del Repositorio
### 3.1. Documentos del TFG
- **Memoria del TFG:** [TFG-PAULAPOLEY.pdf](docs/TFG-PAULAPOLEY.pdf)
- **Presentación del TFG:** [presentacion-TFG-PaulaPoley.pdf](docs/presentacion-TFG-PaulaPoley.pdf)

### 3.2. Código Fuente
- **Aplicación Web:** [`App.py`](src/App.py) - Archivo principal del código de la aplicación web.
- **Código Ejecutado:** [`codigo_ejecutado/`](src/codigo_ejecutado/) - Carpeta con el código ejecutado durante el estudio.

### 3.3. Archivos Adicionales
- **Descripción del Proyecto:** [README.md](README.md) - Este archivo con la descripción general del proyecto.
- **Instrucciones para Ejecutar:** [ejecuta.txt](ejecuta.txt) - Archivo con las instrucciones para ejecutar el proyecto.


## 4. Entorno de Desarrollo
### 4.1. Jupyter Notebook

El entorno de desarrollo elegido para la implementación del sistema es **Jupyter Notebook** utilizada  **Anaconda**, una distribución libre y gratuita diseñada específicamente para la ciencia de datos y el aprendizaje automático.

### 4.2. Visual Studio Code (VS Code)
En el desarrollo de la plataforma web de predicción, se utilizó **Visual Studio Code (VS Code)** el cual permite una integración fluida con herramientas de desarrollo como **Streamlit**, que se utilizó en el proyecto para crear la aplicación web interactiva con Python. 


## 5. Cómo Ejecutar el Proyecto

Para ejecutar este proyecto, sigue las instrucciones detalladas en el archivo [ejecuta.txt](ejecuta.txt).

---

Este repositorio es parte del Trabajo de Fin de Grado de Paula Poley. Para más detalles, revisa la [memoria del TFG](docs/TFG-PAULAPOLEY.pdf) o la [presentación del TFG](docs/presentacion-TFG-PaulaPoley.pdf).


