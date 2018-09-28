import csv
import cv2

if __name__ == "__main__":
    fichero = open("datosCSV.csv", 'w')
    imagen = cv2.imread("pylogo.jpg", 1)
    fichero.write("X,Y,R,G,B\n")
    for y in range(0, imagen.shape[0]):
        for x in range(0, imagen.shape[1]):
            linea = str(x)+","+str(y)+","+str(imagen[y,x][2])+","+str(imagen[y,x][1])+","+str(imagen[y,x][0])+"\n"
            fichero.write(linea)
                