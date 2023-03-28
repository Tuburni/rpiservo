import RPi.GPIO as GPIO
import time

# Configure GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pin connected to the servo motor
servo_pin = 18

# Set up the GPIO pin for output
GPIO.setup(servo_pin, GPIO.OUT)

# Set the frequency for the PWM signal (50Hz is typical for servos)
pwm_frequency = 50
pwm = GPIO.PWM(servo_pin, pwm_frequency)

# Start PWM with a duty cycle of 0 (off)
pwm.start(0)

# Define a function to convert the desired angle to a duty cycle
def angle_to_duty_cycle(angle):
    min_duty_cycle = 2.5  # Duty cycle for 0 degrees
    max_duty_cycle = 12.5  # Duty cycle for 180 degrees
    return ((angle / 180) * (max_duty_cycle - min_duty_cycle)) + min_duty_cycle

try:
    while True:
        # Rotate the servo motor to 0 degrees
        pwm.ChangeDutyCycle(angle_to_duty_cycle(0))
        time.sleep(1)

        # Rotate the servo motor to 90 degrees
        pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
        time.sleep(1)

        # Rotate the servo motor to 180 degrees
        pwm.ChangeDutyCycle(angle_to_duty_cycle(180))
        time.sleep(1)

except KeyboardInterrupt:
    # Stop the PWM signal
    pwm.stop()

    # Clean up the GPIO settings
    GPIO.cleanup()
