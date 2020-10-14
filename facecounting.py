import cv2
import numpy as np
import time
import serial

#Setup Communication path for arduino (In place of 'COM3' put the port to which your arduino is connected)
ard = serial.Serial('COM4', 9600) 
time.sleep(2)
print("Connected to arduino...")

pengklasifikasiWajah  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

videoCam = cv2.VideoCapture(0)

if not videoCam.isOpened():
    print("Kamera tidak dapat diakses")
    exit()

tombolQditekan = False
while (tombolQditekan == False):
    ret, kerangka = videoCam.read()

    if ret == True:
        abuAbu = cv2.cvtColor(kerangka, cv2.COLOR_BGR2GRAY)
        dafWajah = pengklasifikasiWajah.detectMultiScale(abuAbu, scaleFactor = 1.3, minNeighbors = 2)

        for (x, y, w, h) in dafWajah:
            cv2.rectangle(kerangka, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        teks = "Jumlah Orang Terdeteksi = " + str(len(dafWajah))
        
        if len(dafWajah) >= 1 and len(dafWajah) < 3:
            Status = 'L'      
        elif len(dafWajah) >= 3 and len(dafWajah) < 7:
            Status = 'M'    
        elif len(dafWajah) >= 7:
            Status = 'H'
        else :
            Status = 'S'

        ard.write(Status.encode())     
        print("Speed Fan = ", Status)
        time.sleep(0.01)      

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(kerangka, teks, (0, 30), font, 1, (255, 0, 0), 1)
       

        cv2.imshow("Hasil", kerangka)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            tombolQditekan = True
            break

    

videoCam.release()
cv2.destroyAllWindows()