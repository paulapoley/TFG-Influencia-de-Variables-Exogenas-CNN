import streamlit as st
import io
import base64
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.applications.efficientnet import preprocess_input

# Add background image using CSS
image_path = 'D:\\Users\\paula\\Escritorio\\app.png'
image = Image.open(image_path)

# Convert image to bytes
img_byte_arr = io.BytesIO()
image.save(img_byte_arr, format='PNG')

# Convert bytes to base64
image_base64 = base64.b64encode(img_byte_arr.getvalue()).decode()

def main():
    st.set_page_config(
        layout="wide",
        page_title="DermoCheck",
        page_icon="🔍",
        initial_sidebar_state="expanded"
    )
   
    st.sidebar.title("Menú de Navegación")
    st.sidebar.markdown("---")
    
    app_mode = st.sidebar.radio("Seleccione una opción", ["Inicio","Escáner", "Sobre el escáner", "Sobre lesiones cutáneas", "Factores de riesgo", "Prevención y detección precoz"])
   
    if app_mode == "Inicio":
        render_inicio()
    elif app_mode == "Escáner":
        render_escaner()
    elif app_mode == "Sobre el escáner":
        render_sobreescaner()
    elif app_mode == "Sobre lesiones cutáneas":
        render_lesiones()
    elif app_mode == "Factores de riesgo":
        render_factores()
    elif app_mode == "Prevención y detección precoz":
        render_prevencion()
    
    st.sidebar.write("<div style='text-align: center;'><span style='font-size:67px;'></span> <span style='color:black;font-style: italic;font-size:18px;'><br><br><br><br><br><br><br><br><br><br><br>⚠️ Recuerde que esta herramienta proporciona una evaluación inicial y no debe sustituir la consulta médica profesional.</span></div>", unsafe_allow_html=True)

    
def render_inicio():
    st.markdown("<span style='font-size:68px; font-weight: bold; font-family: Arial, sans-serif;'><br>DermoCheck</span>", unsafe_allow_html=True)
    st.markdown("<span style='font-size:30px;'><br>¡Bienvenido a nuestra aplicación de <br> detección de enfermedades de la piel! </span>", unsafe_allow_html=True)
    st.markdown("<span style='font-size:10px;'><br> </span>", unsafe_allow_html=True)

    st.write("<p style='font-size: 24px; font-weight: bold;'>Instrucciones:</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px;'>1. Seleccione la opción escáner en el menú de navegación.</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px;'>2. Cargue una imagen de la lesión cutánea que le preocupa.</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px;'>3. Complete los datos.</p>", unsafe_allow_html=True)
    st.write("<p style='font-size: 20px;'>4. Por último,haga click en realizar predicción para obtener un diagnóstico.</p>", unsafe_allow_html=True)

    
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url('data:image/png;base64,{image_base64}');
                background-size: cover;

            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="background-image"></div>', unsafe_allow_html=True)
    
def render_sobreescaner():
    st.title("Sobre el escáner 📷")
    st.markdown("<hr>", unsafe_allow_html=True)  # Línea horizontal
    st.markdown("""
    <p style='font-size: 16px; color: black;'>
    En nuestra página web, puedes subir una imagen de tu lunar y agregar información sobre factores como edad, sexo, localización de la lesión y tipo de diagnóstico para obtener una clasificación basada en siete clases diferentes de lunares. 
    Utilizando tecnología avanzada de inteligencia artificial, nuestra herramienta puede identificar y clasificar los siguientes tipos de lunares:
    <ol>
    <li style='margin-left: 80px;'><span><b>Nevus melanocíticos</b>: son neoplasias benignas de melanocitos que aparecen en multitud de variantes. A diferencia del melanoma, suelen ser simétricos en color y estructura.</span></li>
    <li style='margin-left: 80px;'><span><b>Melanoma</b>: es una neoplasia maligna de melanocitos, invasiva o in situ, con variantes según sitio anatómico. Caóticos, con criterios específicos. Excluyen variantes no pigmentadas, subungueales, oculares o mucosas.</span></li>
    <li style='margin-left: 80px;'><span><b>Carcinoma basocelular</b>: es un cáncer de piel epitelial común, rara vez metastatiza, pero puede crecer destructivamente sin tratamiento. Tiene variantes: plana, nodular, pigmentada y quística.</span></li>
    <li style='margin-left: 80px;'><span><b>Queratosis actínicas</b>: son lesiones no invasivas que pueden volverse carcinoma. Sin pigmentación y con descamación. Son más comunes en la cara y pueden presentar variantes pigmentadas.</span></li>
    <li style='margin-left: 80px;'><span><b>Lesiones vasculares</b>: incluyen angiomas cereza, angioceratomas, granulomas piogénicos y hemorragias, se distinguen por su color rojo o morado y por la presencia de coágulos rojos o lagunas</span></li>
    <li style='margin-left: 80px;'><span><b>Dermatofibroma</b>: es una lesión cutánea benigna, proliferativa o inflamatoria. Dermatoscópicamente presenta líneas reticulares periféricas y una mancha blanca central indicando fibrosis.</span></li>
    </ol>
    </p>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown(
    '<div style="display: flex; justify-content: center;"><img src="https://raw.githubusercontent.com/paupolceb/streamlit-app/main/tipos.png" alt="Ejemplo de los 7 tipos de lesiones" style="width:900px;"></div>',
    unsafe_allow_html=True)
    st.write("Fuente: [HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000), [HAM10000-description](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6091241/) ")



def render_escaner():
    #ruta
    model_path = 'D:\\Users\\paula\\Escritorio\\TFG\\TFG FINAL - MEMORIA\\modeloApp\\modelo-app.h5'


    # Cargar el modelo
    @st.cache_resource
    def load_saved_model(model_path):
        model = load_model(model_path)
        return model

    model = load_saved_model(model_path)

    # Función para preprocesar la imagen
    def preprocess_image(image):
        image = image.resize((64, 64))  # Cambiar tamaño para que coincida con el tamaño de entrada del modelo
        image = np.array(image)
        image = preprocess_input(image)
        return image
    
    # Función para hacer predicciones
    def predict(image, gender, age, localization, dx_type):
        processed_image = preprocess_image(image)
        # Convertir gender y age a números
        gender_num = 1 if gender == 'male' else 0  # Asignar 1 a masculino y 0 a femenino
        age_num = float(age)  # Convertir edad a float
        # Convertir localization a números
        localization_num = [1 if loc in localization else 0 for loc in ['abdomen', 'scalp', 'back', 'ear', 'face', 
                            'foot', 'hand','lower extremity', 'neck', 'trunk', 'upper extremity', 'unknown']]
        # Asegurar que localization tenga una longitud de 12 (el mismo que en la creación del modelo)
        localization_num += [0] * (12 - len(localization_num))
        # Asegurar que dx_type tenga una longitud de 4 (el mismo que en la creación del modelo)
        dx_type_encoded = [0, 0, 0, 0]  # Inicializar con ceros
        if dx_type == 'histo':
            dx_type_encoded[0] = 1
        elif dx_type == 'consensus':
            dx_type_encoded[1] = 1
        elif dx_type == 'confocal':
            dx_type_encoded[2] = 1
        elif dx_type == 'follow_up':
            dx_type_encoded[3] = 1
        # Concatenar todas las características tabulares
        tabular_input = [gender_num, age_num] + localization_num + dx_type_encoded
        # Asegurar que tabular_input tenga una longitud de 21 (el mismo que en la creación del modelo)
        tabular_input += [0] * (21 - len(tabular_input))
        # Convertir a numpy array
        tabular_input = np.array(tabular_input).reshape(1, -1)
        
        # Modelo toma dos entradas
        prediction = model.predict([np.expand_dims(processed_image, axis=0), tabular_input])
        return np.argmax(prediction)

    # Sección de carga de imagen
    st.header('Cargue la imagen de la lesión cutánea')
    uploaded_image = st.file_uploader('Seleccione o arrastre y suelte la imagen de la lesión cutánea:')

    # Sección de variables exógenas
    st.header('Complete los datos')
    gender = st.radio('Género: ', ['female', 'male', 'unknown'])
    age = st.slider('Edad:', min_value=0, max_value=100, value=30)
    localization = st.multiselect('Localización de la lesión cutánea:', ['abdomen', 'scalp', 'back', 
                                'ear', 'face', 'foot', 'hand','lower extremity', 'neck', 'trunk', 
                                'upper extremity', 'unknown'])
    dx_type = st.multiselect('Tipo de Diagnóstico:', ['histo', 'consensus', 'confocal', 'follow_up'])
    st.markdown("")
    st.markdown("")
    st.markdown("")

    # Botón de predicción
    if uploaded_image is not None and st.button('Realizar predicción'):
        # Verificar si se han completado todos los campos
        if gender != 'unknown' and age != 0 and localization and dx_type:
            st.image(uploaded_image, caption='Imagen de Lesión Cutánea', width=400)
            # Resto del código para la predicción...
            # Codificar dx_type como one-hot
            dx_type_encoded = [0, 0, 0, 0]  # Inicializar con ceros
            if dx_type == 'histo':
                dx_type_encoded[0] = 1
            elif dx_type == 'consensus':
                dx_type_encoded[1] = 1
            elif dx_type == 'confocal':
                dx_type_encoded[2] = 1
            elif dx_type == 'follow_up':
                dx_type_encoded[3] = 1

            # Convertir género y edad a cadenas
            gender = str(gender)
            age = str(age)

            # Definir el diccionario de nombres de clases
            class_names = {
                0: 'Benign keratosis-like lesions',
                1: 'Melanocytic nevi',
                2: 'Dermatofibroma',
                3: 'Melanoma',
                4: 'Vascular lesions',
                5: 'Basal cell carcinoma',
                6: 'Actinic keratoses'
            }

            # Hacer predicción
            prediction_num = predict(Image.open(uploaded_image), gender, age, localization, dx_type_encoded)

            # Obtener el nombre correspondiente a la predicción numérica
            prediction_name = class_names.get(prediction_num, 'Clase Desconocida')

            # Mostrar la predicción
            st.write('<span style="font-size:20px; font-weight:bold;">La predicción es:</span>', prediction_name, unsafe_allow_html=True)
        else:
            st.error("Por favor, complete todos los datos antes de realizar la predicción.")
    elif uploaded_image is None and st.button('Realizar predicción'):
        st.error("Por favor, cargue una imagen antes de realizar la predicción.")


def render_lesiones():
    st.title("Sobre lesiones cutáneas 📚")
    st.markdown("<hr>", unsafe_allow_html=True)  # Línea horizontal
    st.markdown("<p style='font-size:18px; color:black;'>La piel es el órgano más grande del cuerpo humano, actuando como una barrera protectora contra agentes externos como bacterias y sustancias químicas. Contiene melanina, que protege contra los rayos ultravioleta, y regula la temperatura corporal. Aunque la mayoría de las lesiones cutáneas no son graves, algunas pueden ser severas y representar un riesgo para la vida.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px; color:balck;'><strong><em>Es fundamental monitorear cualquier cambio en la piel y consultar a un médico ante la presencia de lesiones sospechosas, ya que pueden ser benignas o malignas.</em></p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size:18px; color:balck;'><br>La imagen adjunta proporciona una representación visual de la diferenciación entre tumores benignos y malignos.</p>", unsafe_allow_html=True)
    st.markdown("""<div style='margin-left: 30px;'>
      <ul>
        <li>En 'Benign Tumor', se muestra una célula que ilustra la naturaleza no cancerosa de este tipo de tumor, caracterizada por su incapacidad para propagarse a otros tejidos o órganos</li>
        <li>Por otro lado, en 'Malignant Tumor', se representa otra célula que refleja la naturaleza cancerosa de este tipo de tumor, con la capacidad de diseminarse a través del cuerpo, afectando otros tejidos y órganos</li>
      </ul>
    </div>""", unsafe_allow_html=True)

    st.markdown(
    '<div style="display: flex; justify-content: center;">'
    '<img src="https://i.pinimg.com/736x/08/8e/b3/088eb3cb3c50cf0953156bd37d51e40a.jpg" '
    'alt="Benign Tumor vs Malignant Tumor" style="width:700px;">'
    '</div>',
    unsafe_allow_html=True)
    st.write("Fuentes: [Universidad Europea](https://universidadeuropea.com/blog/tipos-lesiones-piel/) | "
            "[Imagen](https://medicinabasica.com/diferencias-entre-un-tumor-maligno-y-benigno)")

def render_factores():
    st.title("Factores de riesgo 🔍")
    st.markdown("<hr>", unsafe_allow_html=True)  # Línea horizontal
    st.markdown("<p style='font-size:18px; color:black;'>Los factores de riesgo para las lesiones cutáneas pueden variar desde la exposición al sol hasta antecedentes familiares de cáncer de piel. Aquí hay algunos factores de riesgo comunes a considerar:</p>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
    <li style='font-size:18px; color:black;'>Exposición a la radiación ultravioleta (UV) del sol o camas de bronceado.</li>
    <li style='font-size:18px; color:black;'>Antecedentes familiares de cáncer de piel.</li>
    <li style='font-size:18px; color:black;'>Piel clara que se quema fácilmente o no se broncea.</li>
    <li style='font-size:18px; color:black;'>Presencia de lunares atípicos o un gran número de lunares.</li>
    <li style='font-size:18px; color:black;'>Antecedentes personales de quemaduras solares graves.</li>
    <li style='font-size:18px; color:black;'>Inmunosupresión debido a condiciones como el VIH/SIDA o el uso de medicamentos inmunosupresores.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:18px; color:black;'>Es importante tener en cuenta estos factores de riesgo y tomar medidas preventivas, como usar protector solar, ropa protectora y evitar la exposición excesiva al sol durante las horas pico de radiación UV.</p>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("<p style='font-size:18px; color:black;'>Para obtener más información sobre el cáncer de piel, sus causas, síntomas y prevención, se puede consultar el vídeo proporcionado por la AECC (Asociación Española Contra el Cáncer):", unsafe_allow_html=True)
    st.markdown('<iframe width="640" height="360" src="https://www.youtube.com/embed/Tp_WaONfEIU" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.write("Fuente: [Asociación española contra el cáncer](https://www.contraelcancer.es/es/todo-sobre-cancer/tipos-cancer/cancer-piel)")
    

def render_prevencion():
    st.title("Prevención y detección precoz ☀️")
    st.markdown("<hr>", unsafe_allow_html=True)  # Línea horizontal
    st.markdown("<p style='font-size:18px; color:black;'>La prevención y detección temprana son fundamentales para reducir el riesgo de desarrollar lesiones cutáneas malignas. Aquí hay algunas estrategias importantes:</p>", unsafe_allow_html=True)
    st.markdown("""
    <ul>
    <li style='font-size:18px; color:black;'>Usar protector solar con un SPF (factor de protección solar) de al menos 30, reaplicándolo cada dos horas y después de nadar o sudar.</li>
    <li style='font-size:18px; color:black;'>Vestir ropa protectora, como sombreros de ala ancha y camisas de manga larga.</li>
    <li style='font-size:18px; color:black;'>Evitar la exposición al sol durante las horas pico de radiación UV, generalmente entre las 10 a.m. y las 4 p.m.</li>
    <li style='font-size:18px; color:black;'>Realizar autoexámenes regulares de la piel para detectar cualquier cambio en la apariencia de lunares o lesiones cutáneas.</li>
    <li style='font-size:18px; color:black;'>Programar exámenes regulares con un dermatólogo, especialmente si tiene antecedentes familiares de cáncer de piel o factores de riesgo adicionales.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size:18px; color:black;'>Al seguir estas recomendaciones y estar atento a los signos de advertencia, puede ayudar a proteger su piel y detectar cualquier problema de manera temprana, lo que aumenta las posibilidades de un tratamiento exitoso.</p>", unsafe_allow_html=True)
    st.write("<p style='font-size:18px; color:black;'><strong><br> Se adjunta vídeo sobre la regla del ABCD para la autoexploración:" , unsafe_allow_html=True)
    st.markdown('<iframe width="640" height="360" src="https://www.youtube.com/embed/B_7L6P5m_BI" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.write("Fuente: [Asociación española contra el cáncer](https://www.contraelcancer.es/es/todo-sobre-cancer/tipos-cancer/cancer-piel)")

if __name__ == "__main__":
    main()
