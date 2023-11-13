from PIL import Image
import numpy as np

# Cargar las imágenes

opt1 = str(input("Imagen 1: "))
opt2 = str(input("Imagen 1: "))

img1 = Image.open(opt1)
img2 = Image.open(opt2)

# Convertir a array de NumPy
array1 = np.array(img1)
array2 = np.array(img2)

# Comprobar si ambas imágenes tienen las mismas dimensiones
if array1.shape != array2.shape:
    print("[!] ERROR: Las imagenes deben ser del mismo tamaño")
else:
    # Realizar la operación XOR en cada byte de los canales RGB, NumPy ya trae esta función xd
    xor_result = np.bitwise_xor(array1, array2)

    # Convertir el array resultante de nuevo a una imagen, guarda el xor anterior
    xor_image = Image.fromarray(np.uint8(xor_result))

    # Mostrar y guardar la imagen resultante
    opt3 = str(input("Guardar imagen en: "))
    xor_image.save(opt3)
    xor_image.show(opt3)
