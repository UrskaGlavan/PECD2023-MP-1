import RPi.GPIO as GPIO
import io
from picamera2 import Picamera2
import cv2
import numpy
import time

PIR_SENSOR  = 12
BUZZER_PIN = 7

notes = {   
   'A3':  220.00,  
   'C4':  261.63,
   'G4':  392.00, 
   'D4':  293.66,
   'E4':  329.63,
   'F4':  349.23,   
   'A4':  440.00,
}
note_sequence = ['D4', 'A4', 'A4', 'F4', 'E4', 'D4','C4', 'A3','C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4','D4']             
note_duration = [100, 150, 50, 50, 50, 100, 90, 50,  50, 100, 50,50, 50, 50, 100, 190] 


disappointing_melody = ['A4', 'A3']
disappointing_duration = [100, 200]

def play_sound(duration, frequency):
    period = 1.0 / frequency 
    for i in range(duration):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(period / 2)  
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(period / 2)  
        
        
        
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(PIR_SENSOR, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
    
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cv2.startWindowThread()

picam2 = Picamera2()

#low quality
#picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (320, 240)})) 

#umes
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (1280, 720)}))


#high quality
#picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (1920, 1080)}))


i = 0



try: # Start of a loop
         while True:
                 if(GPIO.input(PIR_SENSOR) == 0): # When Sensor Input = 0
                         print("Ni gibanja ...") # When the print command is exe>
                         time.sleep(0.5) # wait 0,5 second
                 elif(GPIO.input(PIR_SENSOR) == 1): # When Sensor Input = 1
                        
                         print("Gibanje zaznano!")
                         picam2.start()
                         im = picam2.capture_array()
                         grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                         faces = face_detector.detectMultiScale(grey, 1.3, 5)   
                         i = 1 + i  
                         for (x,y,w,h) in faces:
                           cv2.rectangle(im,(x,y),(x+w,y+h),(255,255,0),2)
                         cv2.imshow("Camera", im)
                         
                         cv2.waitKey(1)
                         if len(faces) > 0:   
                                                  
                           print("Pojem pesem")
                           print(i , "Face detected.")
                           for duration,n in zip(note_duration,note_sequence):
                             play_sound(duration, notes[n])
                           time.sleep(1)
                         else:
                           print(i,"No face detected.") 
                           if (i == 3):                             
                             for duration, n in zip(disappointing_duration, disappointing_melody):
                               play_sound(duration, notes[n])
                             i = 0                         
                 time.sleep(0.5) # wait 0,5 second
                 picam2.stop()
                   
except KeyboradInterrupt:
         
         
         GPIO.cleanup()
         