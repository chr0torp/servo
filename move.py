import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servol = GPIO.PWM(11, 50)  # GPIO 11 for PWM with 50Hz frequency

servol.start(0)  # Initialize with 0% duty cycle (0 degrees)

time.sleep(2)  # Wait before stopping the servo

servol.ChangeDutyCycle(12)  
time.sleep(2)

servol.ChangeDutyCycle(4)
time.sleep(2)

servol.ChangeDutyCycle(0)  

servol.stop()  # Stop the servo
GPIO.cleanup()  # Clean up GPIO settings
print("Servo movement completed and GPIO cleaned up.")
