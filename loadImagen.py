import csv
import cv2

if __name__ == "__main__":
    file = open("dataCSV.csv", 'w')
    image = cv2.imread("pylogo.jpg", 1)
    file.write("X,Y,R,G,B\n")
    for y in range(0, image.shape[0]):
        for x in range(0, image.shape[1]):
            line = str(x)+","+str(y)+","+str(image[y,x][2])+","+str(image[y,x][1])+","+str(image[y,x][0])+"\n"
            file.write(line)
    file.close()
                