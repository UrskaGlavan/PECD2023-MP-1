import RPi.GPIO as GPIO
import time

BUZZER_PIN = 7  # Buzzer pin number


def play_sound(duration, frequency):
    period = 1.0 / frequency  # Calculate the period for the given frequency
    for i in range(duration):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(period / 2)  # Use half of the period for HIGH
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(period / 2)  # Use half of the period for LOW

'''
def play_sound(duration, frequency):  # Play different frequencies
    for i in range(duration):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(frequency)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(frequency)
'''

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

notes = {
   'C0':  16.35,
   'Db0': 17.32,
   'D0':  18.35,
   'Eb0': 19.45,
   'E0':  20.60,
   'F0':  21.83,
   'Gb0': 23.12,
   'G0':  24.50,
   'Ab0': 25.96,
   'A0':  27.50,
   'Bb0': 29.14,
   'B0':  30.87,
   'C1':  32.70,
   'Db1': 34.65,
   'D1':  36.71,
   'Eb1': 38.89,
   'E1':  41.20,
   'F1':  43.65,
   'Gb1': 46.25,
   'G1':  49.00,
   'Ab1': 51.91,
   'A1':  55.00,
   'Bb1': 58.27,
   'B1':  61.74,
   'C2':  65.41,
   'Db2': 69.30,
   'D2':  73.42,
   'Eb2': 77.78,
   'E2':  82.41,
   'F2':  87.31,
   'Gb2': 92.50,
   'G2':  98.00,
   'Ab2': 103.83,
   'A2':  110.00,
   'Bb2': 116.54,
   'B2':  123.47,
   'C3':  130.81,
   'Db3': 138.59,
   'D3':  146.83,
   'Eb3': 155.56,
   'E3':  164.81,
   'F3':  174.61,
   'Gb3': 185.00,
   'G3':  196.00,
   'Ab3': 207.65,
   'A3':  220.00,
   'Bb3': 233.08,
   'B3':  246.94,
   'C4':  261.63,
   'Db4': 277.18,
   'D4':  293.66,
   'Eb4': 311.13,
   'E4':  329.63,
   'F4':  349.23,
   'Gb4': 369.99,
   'G4':  392.00,
   'Ab4': 415.30,
   'A4':  440.00,
   'Bb4': 466.16,
   'B4':  493.88,
   'C5':  523.25,
   'Db5': 554.37,
   'D5':  587.33,
   'Eb5': 622.25,
   'E5':  659.26,
   'F5':  698.46,
   'Gb5': 739.99,
   'G5':  783.99,
   'Ab5': 830.61,
   'A5':  880.00,
   'Bb5': 932.33,
   'B5':  987.77,
   'C6':  1046.50,
   'Db6': 1108.73,
   'D6':  1174.66,
   'Eb6': 1244.51,
   'E6':  1318.51,
   'F6':  1396.91,
   'Gb6': 1479.98,
   'G6':  1567.98,
   'Ab6': 1661.22,
   'A6':  1760.00,
   'Bb6': 1864.66,
   'B6':  1975.53,
   'C7':  2093.00,
   'Db7': 2217.46,
   'D7':  2349.32,
   'Eb7': 2489.02,
   'E7':  2637.02,
   'F7':  2793.83,
   'Gb7': 2959.96,
   'G7':  3135.96,
   'Ab7': 3322.44,
   'A7':  3520.01,
   'Bb7': 3729.31,
   'B7':  3951.07,
   'C8':  4186.01,
   'Db8': 4434.92,
   'D8':  4698.64,
   'Eb8': 4978.03,
}

# Your notes sequence
note_sequence = ['D4', 'A4', 'A4', 'F4', 'E4', 'D4',
                 'C4', 'A3','C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4','C4',
                 ##prvi del
                 'D4', 'A4', 'A4', 'F4', 'E4', 'D4',
                 'C4', 'A3','C4', 'D4', 'E4', 'F4', 'G4', 'F4', 'E4','D4']
                 
note_duration = [100, 150, 50, 50, 50, 100,
                 90, 50,  50, 100, 50,50, 50, 50, 100, 190,
                 #100, 150, 50, 50, 50, 100, 100, 50, 50, 100,
                 #50, 50, 50, 50, 100, 200
                 ]       
                 

for duration,n in zip(note_duration,note_sequence):
    play_sound(duration, notes[n])

GPIO.cleanup()  # Clear GPIO

