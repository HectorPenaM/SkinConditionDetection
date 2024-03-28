from flask import Flask, render_template, request
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.metrics import confusion_matrix
import seaborn as sns

app = Flask(__name__)

# Definir transformaciones para la imagen
transformacion = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Ruta al archivo de pesos del modelo
ruta_modelo = 'model_weights_18'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnosticar', methods=['POST'])
def diagnosticar():
    # Obtener la imagen cargada por el usuario
    imagen = request.files['imagen']
    ruta_imagen = os.path.join('static', imagen.filename)
    imagen.save(ruta_imagen)
    
    # Abrir la imagen y aplicar transformaciones
    imagen_pil = Image.open(imagen)
    imagen_tensor = transformacion(imagen_pil).unsqueeze(0)  # Añadir dimensión del lote
    
    # Crear modelo y modificar la última capa lineal para 4 clases
    modelo = models.resnet18()
    num_ftrs = modelo.fc.in_features
    modelo.fc = nn.Linear(num_ftrs, 4)  # Cambiar 4 al número de clases en tu conjunto de datos
    
    # Cargar pesos del modelo desde la ruta especificada
    modelo.load_state_dict(torch.load(ruta_modelo))
    modelo.eval()

    # Realizar la clasificación de la imagen con el modelo
    with torch.no_grad():
        # Pasar la imagen a través del modelo
        resultados = modelo(imagen_tensor)
        
        # Obtener la clase predicha (índice del valor máximo)
        _, clase_predicha = resultados.max(1)
        
        # Convertir el índice de la clase predicha a una etiqueta legible
        etiqueta_predicha = obtener_etiqueta(clase_predicha.item())
        
        # Obtener la probabilidad de la clase predicha
        probabilidad_predicha = resultados.softmax(dim=1)[0, clase_predicha].item()
    
    # Generar el resultado del diagnóstico
        # Formatear los resultados del diagnóstico
    resultado_diagnostico = {
        "nombre": etiqueta_predicha["nombre"],
        "probabilidad": f"{probabilidad_predicha:.2f}",
        "definicion": etiqueta_predicha["definicion"],
        "tratamiento": etiqueta_predicha["tratamiento"].split(", ")  # Convertir el tratamiento a una lista
    }
    
    # Devolver los resultados al usuario, incluyendo la ruta de la imagen cargada
    return render_template('index.html', imagen_cargada=imagen.filename, resultado_diagnostico=resultado_diagnostico)
    

def obtener_etiqueta(indice_clase):
    # Definir las etiquetas y sus descripciones
    etiquetas = {
        0: {"nombre": "Acné", "definicion": "El acné es una afección cutánea común que provoca granos. Se produce cuando los folículos pilosos, poros o glándulas sebáceas de la piel se obstruyen con sebo y células cutáneas muertas.", "tratamiento": "El tratamiento del acné puede incluir el uso de medicamentos tópicos, antibióticos, anticonceptivos orales y procedimientos médicos."},
        1: {"nombre": "Eczema", "definicion": "El eccema, también conocido como dermatitis, es una inflamación de la piel que provoca picazón, enrojecimiento, descamación y ampollas.", "tratamiento": "El tratamiento del eccema puede incluir el uso de cremas y ungüentos, antihistamínicos, corticosteroides tópicos y fototerapia."},
        2: {"nombre": "Piel Saludable", "definicion": "La piel saludable se caracteriza por tener una apariencia clara y sin problemas. Es importante mantener una buena rutina de cuidado de la piel para prevenir afecciones cutáneas y mantener la piel en óptimas condiciones.", "tratamiento": "El tratamiento para mantener la piel saludable incluye el uso de limpiadores suaves, humectantes, protección solar y una dieta equilibrada."},
        3: {"nombre": "Melanoma", "definicion": "El melanoma es un tipo de cáncer de piel que se desarrolla a partir de los melanocitos, las células que producen melanina. Puede comenzar como un lunar o una mancha anormal en la piel.", "tratamiento": "El tratamiento del melanoma puede incluir cirugía para extirpar el tumor, radioterapia, terapia dirigida y terapia inmunológica."},
        
    }
    return etiquetas.get(indice_clase, {"nombre": "Clase Desconocida", "definicion": "No se encontró información sobre esta clase.", "tratamiento": "No se encontró información sobre el tratamiento de esta clase."})


if __name__ == '__main__':
    # Cambiar '0.0.0.0' a tu dirección IP pública
    app.run(host='194.113.64.36', port=5000)
