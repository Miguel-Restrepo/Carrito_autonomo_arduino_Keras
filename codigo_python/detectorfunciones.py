import serial
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import cv2
import time
# load the trained model to classify sign
from keras.models import load_model
model = load_model('traffic_classifier.h5')
cap = cv2.VideoCapture(0)
classes = {1: 'Límite de velocidad (20 km/h)',
           2: 'Límite de velocidad (30 km/h)',
           3: 'Límite de velocidad (50 km/h)',
           4: 'Límite de velocidad (60 km/h)',
           5: 'Límite de velocidad (70 km/h)',
           6: 'Límite de velocidad (80 km/h)',
           7: 'Fin del límite de velocidad (80 km/h)',
           8: 'Límite de velocidad (100 km/h)',
           9: 'Límite de velocidad (120 km/h)',
           10: 'Prohibido pasar',
           11: 'Prohibido pasar vehículos de más de 3.5 toneladas',
           12: 'Derecho de paso en la intersección',
           13: 'Carretera prioritaria',
           14: 'Rendimiento',
           15: 'Alto',
           16: 'Sin vehículos',
           17: 'Vehículo > 3.5 toneladas prohibido',
           18: 'No entre',
           19: 'Precaución general',
           20: 'Curva peligrosa a la izquierda',
           21: 'Curva peligrosa a la derecha',
           22: 'Doble curva',
           23: 'Camino lleno de baches',
           24: 'Camino resbaladizo',
           25: 'El camino se estrecha a la derecha',
           26: 'Obras viales',
           27: 'Semáforos',
           28: 'peatones',
           29: 'Cruce de niños',
           30: 'Cruce de bicicletas',
           31: 'Cuidado con el hielo/la nieve',
           32: 'Cruce de animales salvajes',
           33: 'Velocidad final + límites de paso',
           34: 'Gira a la derecha adelante',
           35: 'Gira a la izquierda adelante',
           36: 'Solo adelante',
           37: 'Ir recto o a la derecha',
           38: 'Ir recto o a la izquierda',
           39: 'Manténgase a la derecha',
           40: 'Manténgase a la izquierda',
           41: 'Rotonda obligatoria',
           42: 'Fin de no pasar',
           43: 'Terminar sin vehículos de paso > 3.5 toneladas'}


texto = "Sin identificar"
ubicacion = (50, 50)
font = cv2.FONT_HERSHEY_TRIPLEX
tamañoLetra = 2
colorLetra = (255, 255, 255)
grosorLetra = 1

#senal=classify('C:/Users/migue/PycharmProjects/comunicacion_datos/imagen_prueba.png')

def classify(file_path):
    global label_packed
    print(file_path)
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred = np.argmax(model.predict([image]), axis=1)[0]
    print("pred:")
    print(pred)

    return pred
try:
    #PUERTO por el q se conecto
    BT = serial.Serial('COM8',115200)
    print("conectado")
except:
    print("Conexion fallida con el modulo bluetooth")
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    cv2.imwrite("C:/Users/migue/PycharmProjects/comunicacion_datos/imagen_prueba.png", image)
    time.sleep(2)
    pred = classify('C:/Users/migue/PycharmProjects/comunicacion_datos/imagen_prueba.png')
    print("pred:")
    print(pred)
    sign = classes[pred]
    print("señal")
    print(sign)
    texto=sign
    singarduino ='z'
    # Escribir texto
    if pred==2:#reducir 30
        singarduino = 'a'
    elif pred==4:#reducir 60
        singarduino = 'b'
    elif pred==15:#pare
        singarduino = 'c'
    elif pred==34:#derecha
        singarduino = 'd'
    elif pred==35:#izquierda
        singarduino = 'e'
    elif pred==36:#siga
        singarduino = 'f'
    elif pred==28:#cruce peatones
        singarduino = 'g'
    cv2.putText(image, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
    try:
        BT.write(singarduino.encode('uft-8'))
    except:
        print("no blue")
    cv2.imshow('Vista carrito', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()


