import cv2
import numpy as np
import pygame

fire = 0
alarm_status = False
 #play Sound
#def alarm():
 #   playsound.playsound()
def play_alarm(alarm_file):
    pygame.mixer.init()
    pygame.mixer.music.load(alarm_file)
    pygame.mixer.music.play()
alarm_file = "Alarm-Fast-A1-www.fesliyanstudios.com.mp3"



cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    frame = cv2.resize(frame,(800,600))
    blur = cv2.GaussianBlur(frame,(15,15),0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)


    lower = [18,50,50]
    upper = [30,255,255]

    lower = np.array(lower,dtype='uint8')
    upper = np.array(upper,dtype='uint8')

    mask = cv2.inRange(hsv,lower,upper)

    output = cv2.bitwise_and(frame,hsv,mask=mask)

    #measuring fire treshold
    n_t = cv2.countNonZero(mask)

    if int(n_t) > 15000:
        print("Fire")
        fire = fire + 1
        if fire >= 1:
           
           if alarm_status == False:
               play_alarm(alarm_file)
               alarm_status = True
    


    if ret == False:
        break
    cv2.imshow('video',output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
