import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
servol = GPIO.PWM(11, 50)  # GPIO 11 for PWM with 50Hz frequency

servol.start(0)  # Initialize with 0% duty cycle (0 degrees)
time.sleep(2)  # Allow servos to initialize

duty = 2 

while duty <= 12:
    servol.ChangeDutyCycle(duty)  # Move servo to duty cycle (angle)
    time.sleep(1)  # Wait for servo to reach position
    duty += 1  # Increment duty cycle for next position

time.sleep(2)  # Wait before stopping the servo

servol.ChangeDutyCycle(7)  
time.sleep(2)

servol.ChangeDutyCycle(2)
time.sleep(2)
servol.ChangeDutyCycle(0)  

servol.stop()  # Stop the servo
GPIO.cleanup()  # Clean up GPIO settings
print("Servo movement completed and GPIO cleaned up.")
