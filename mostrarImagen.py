import csv
import cv2
import numpy

if __name__ == "__main__":
    with open("datosCSV.csv") as buscarUL:
        ultimaLinea = buscarUL.readlines()[-1]
        print(ultimaLinea)
        ultimaLinea = ultimaLinea.split(",")
        tamX = int(ultimaLinea[0])
        tamY = int(ultimaLinea[1])
    with open("datosCSV.csv") as baseCSV:
        print(tamX,tamY)
        #imagen = cv2.imread("pybase.jpg", 1)
        lector = csv.reader(baseCSV, delimiter=',')
        imagen = numpy.ones((tamY+1,tamX+1,3),numpy.uint8)*255
        #cv2.imshow('imagen',imagen)
        linea = 0
        #cv2.waitKey();
        for row in lector:
            if linea == 0:
                linea += 1
            else:
                imagen.itemset((int(row[1]),int(row[0]),0),int(row[4]))
                imagen.itemset((int(row[1]),int(row[0]),1),int(row[3]))
                imagen.itemset((int(row[1]),int(row[0]),2),int(row[2]))
                linea += 1
        cv2.imshow('imagenCargada', imagen)
        cv2.waitKey()