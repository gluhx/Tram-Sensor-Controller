import RPi.GPIO as GPIO
import time

led_pin = 18

def init_GPIO():
    # Настройка режима нумерации пинов
    GPIO.setmode(GPIO.BCM)  # или GPIO.BOARD

    # Настроить пин как выход
    GPIO.setup(led_pin, GPIO.OUT)

def led_off():
    try:
        while True:
            GPIO.output(led_pin, GPIO.LOW)   # Выключить
    except KeyboardInterrupt:
        print("Программа остановлена")
    finally:
        GPIO.cleanup()  # Всегда очищайте пины!

def led_on():
    try:
        GPIO.output(led_pin, GPIO.HIGH)  # Включить
    except KeyboardInterrupt:
        print("Программа остановлена")
    finally:
        GPIO.cleanup()  # Всегда очищайте пины!