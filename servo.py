import RPi.GPIO as GPIO
import time

# встановлюємо режим номерації BCM
GPIO.setmode(GPIO.BCM)

# встановлюємо номер піна, який буде використовуватися для керування сервомотором
servo_pin = 18

# встановлюємо пін на вихід
GPIO.setup(servo_pin, GPIO.OUT)

# створюємо об'єкт PWM з частотою 50 Гц
pwm = GPIO.PWM(servo_pin, 50)

# стартуємо PWM з duty cycle 0 (повністю закритий)
pwm.start(0)

# функція для перетворення кута в duty cycle
def angle_to_duty_cycle(angle):
    duty_cycle = (0.05 * angle) + 2.5
    return duty_cycle

# рухаємо сервомотор на 90 градусів
pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
time.sleep(1)

# рухаємо сервомотор на 0 градусів
pwm.ChangeDutyCycle(angle_to_duty_cycle(0))
time.sleep(1)

# рухаємо сервомотор на 180 градусів
pwm.ChangeDutyCycle(angle_to_duty_cycle(180))
time.sleep(1)

# зупиняємо PWM
pwm.stop()

# вимикаємо GPIO
GPIO.cleanup()
