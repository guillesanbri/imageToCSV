import csv
import cv2
import numpy as np

if __name__ == "__main__":
    with open("dataCSV.csv") as findLL:
        lastLine = findLL.readlines()[-1]
        lastLine = lastLine.split(",")
        sizeX = int(lastLine[0])
        sizeY = int(lastLine[1])
    with open("dataCSV.csv") as baseCSV:
        reader = csv.reader(baseCSV, delimiter=',')
        image = np.ones((sizeY+1,sizeX+1,3),np.uint8)*255
        line = 0
        for row in reader:
            if line == 0:
                line += 1
            else:
                image.itemset((int(row[1]),int(row[0]),0),int(row[4]))
                image.itemset((int(row[1]),int(row[0]),1),int(row[3]))
                image.itemset((int(row[1]),int(row[0]),2),int(row[2]))
                line += 1
        cv2.imshow('loadedImage', image)
        cv2.waitKey()