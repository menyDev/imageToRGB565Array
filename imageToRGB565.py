import numpy as np
import cv2

#información de formato RGB565
#https://www.barth-dev.de/about-rgb565-and-how-to-convert-into-it/

#convierte las componentes del pixel a formato RGB565 y retorna un entero
def toIntRGB565(red, green, blue):
    res = int(0)
    res = (((red & 0b11111000)<<8) + ((green & 0b11111100)<<3) + (blue>>3))
    return res

#definición de constantes
height = 64 #num de pixeles de alto en la imagen (filas)
width = 64 #num de pixeles de ancho en la imagen (columnas)

arrayRGB565 = np.zeros((height,width))

# carga imagen en BGR, OJO!!!! Es BGR No RGB
img = cv2.imread('PixelArt.png')
#tamaño de la imagen, coincide con el de la matrix que tenemos
dim = (width, height)
# cambiamos tamaño de imagen
img64 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#se gudara imagen de 64x64
#cv2.imwrite("art64.png",img64)

#separamos en canales BGR
canalB,canalG,canalR = cv2.split(img64)

#recorre toda la imagen
for row in range(height):
    for col in range(width):
        arrayRGB565[row][col] = toIntRGB565(canalR[row][col],canalG[row][col],canalB[row][col])

#este array se deberá enviar a la base de datos, son los valores de cada pixel en la matrix
arrayFinal = arrayRGB565.reshape(width*height)