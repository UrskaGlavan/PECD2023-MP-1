import RPi.GPIO as GPIO
import sys 
import signal 

PIR_SENSOR  = 12

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    
def sensor_callback(channel):
    if GPIO.input(PIR_SENSOR) == 1:  # Zazna samo dvig stanja
            print("Gibanje zaznano!")
            
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(PIR_SENSOR, GPIO.IN)
    
    GPIO.add_event_detect(PIR_SENSOR, GPIO.RISING, 
            callback=sensor_callback, bouncetime=1)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()