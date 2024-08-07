# Trabajo Fin de Grado 
Este repositorio contiene el código, documentación y recursos relacionados con el Trabajo de Fin de Grado sobre la detección de enfermedades cutáneas mediante redes neuronales convolucionales (CNN). El proyecto incluye una aplicación web para la evaluación de lesiones cutáneas.

**Título** = Influencia de Variables Exógenas en la Detección de Enfermedades de Piel mediante Redes Neuronales y Análisis de Imágenes Médicas.

**Objetivo del Estudio**
Este Trabajo de Fin de Grado estudia cómo variables exógenas afectan la capacidad predictiva de los modelos de clasificación de imágenes. Se centra en la mejora de la precisión y eficacia en la detección de enfermedades cutáneas mediante el uso de redes neuronales convolucionales (CNN) y la inclusión de variables exógenas, tales como la ubicación de la lesión, la edad, el sexo del paciente y el tipo de diagnóstico. 

**Metodología**
Se desarrollaron dos enfoques de detección utilizando CNN:

-Modelo Sin Variables Exógenas: Un enfoque tradicional basado únicamente en las características visuales de las imágenes de lesiones cutáneas.
-Modelo Con Variables Exógenas: Un enfoque mejorado que incorpora datos adicionales (ubicación de la lesión, edad, sexo y diagnóstico) para refinar la clasificación.

Se utilizaron varias arquitecturas de modelos preentrenados, como DenseNet121, MobileNetV2, ResNet50, EfficientNetB0, Xception, así como una CNN diseñada desde cero. Estos modelos se entrenaron con una colección de imágenes de alta resolución de lesiones cutáneas etiquetadas, abarcando siete afecciones dermatológicas distintas.

## Contenidos

- **Documentos del TFG --> /docs**:
  - [TFG-PAULAPOLEY.pdf](docs/TFG-PAULAPOLEY.pdf): Memoria del TFG.
  - [presentacion-TFG-PaulaPoley.pdf](docs/presentacion-TFG-PaulaPoley.pdf): Presentación del TFG.

- **Código Fuente --> /src**:
  - `App.py` en la carpeta `src`: Archivo principal del código de la aplicación web.
  - `codigo_ejecutado/` en la carpeta `src`: Carpeta que contiene el código ejecutado.

- **Archivos Adicionales**:
  - [readme.md](README.md): Este archivo con la descripción del proyecto.
  - [ejecuta.txt](ejecuta.txt): Archivo con instrucciones para ejecutar el proyecto.


