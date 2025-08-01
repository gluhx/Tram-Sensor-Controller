import RPi.GPIO as GPIO
import time

# Глобальная переменная для хранения пина
LED_PIN = 18 

def init_GPIO(pin):
    """
    Инициализирует GPIO для светодиода.
    
    :param pin: Номер GPIO пина (по BCM)
    """
    global LED_PIN
    LED_PIN = pin
    
    GPIO.setmode(GPIO.BCM)              # Режим нумерации GPIO
    GPIO.setup(LED_PIN, GPIO.OUT)       # Настраиваем пин как выход
    led_off()                      # Выключаем светодиод при старте
    print(f"GPIO {LED_PIN} инициализирован как выход для светодиода.")

def led_on():
    """
    Включает светодиод.
    """
    if LED_PIN is None:
        print("Ошибка: светодиод не инициализирован!")
        return
    GPIO.output(LED_PIN, GPIO.HIGH)
    print(f"Светодиод на GPIO {LED_PIN} включён.")

def led_off():
    """
    Выключает светодиод.
    """
    if LED_PIN is None:
        print("Ошибка: светодиод не инициализирован!")
        return
    GPIO.output(LED_PIN, GPIO.LOW)
    print(f"Светодиод на GPIO {LED_PIN} выключен.")
