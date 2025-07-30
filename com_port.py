import serial
import time

def init_com(baudrate):
    ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate=baudrate,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    return ser

def send_com(text, serial):
    try:
        # Отправка данных
        serial.write(b'Hello Pi!\n')
        
        # Чтение ответа
        if serial.in_waiting > 0:
            data = serial.readline()
            print("Получено:", data.decode('utf-8').strip())
    except KeyboardInterrupt:
        print("Завершено")
    finally:
        serial.close()