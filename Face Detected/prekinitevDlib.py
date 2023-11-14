import RPi.GPIO as GPIO
import sys 
import signal 
from picamera2 import Picamera2
import cv2
import time
import dlib

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

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    
def sensor_callback(channel):
    if GPIO.input(PIR_SENSOR) == 1:
      
      print("Gibanje zaznano!")
      image = picam2.capture_array()
      gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      faces = detector(gray_image)
      for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
      cv2.imshow("Camera", image)
      cv2.waitKey(1)
      if len(faces) > 0:
        print("Pojem pesem")
        print("Face detected.")
        #for duration,n in zip(note_duration,note_sequence):
          #play_sound(duration, notes[n])
      else:
        print("No face detected.")         
          
               
def play_sound(duration, frequency):
    period = 1.0 / frequency 
    for i in range(duration):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(period / 2)  
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(period / 2)  
        
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)    
    GPIO.setup(PIR_SENSOR, GPIO.IN)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    
    detector = dlib.get_frontal_face_detector()
    cv2.startWindowThread()

    picam2 = Picamera2()
    #camera_config = picam2.create_still_configuration(main={"size":(320,240)})
    #picam2.configure(camera_config)
    #picam2.configure(picam2.create_preview_configuration(main={"format":'XRGB8888', "size": (640,480)}))
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam2.start()
    
     
    GPIO.add_event_detect(PIR_SENSOR, GPIO.RISING, callback=sensor_callback, bouncetime=1)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    GPIO.cleanup()
    
    
    
    


  







      
                 



  

    