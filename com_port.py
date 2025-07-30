import serial
import time
import config

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
        serial.write(bytes(text, "utf-8"))
        
        # Чтение ответа
        if serial.in_waiting > 0:
            data = serial.readline()
            print("Получено:", data.decode('utf-8').strip())
    except KeyboardInterrupt:
        print("Завершено")
    finally:
        serial.close()

def listen_com(serial, callback):
    try:
        while True:
            if serial.in_waiting > 0:
                line = serial.readline().decode('utf-8', errors='ignore').strip()
                if line:
                    callback(line)
            time.sleep(0.01)
    except Exception as e:
        print(f"Ошибка: {e}")

def command(command, serial):
    
    if "set interval " in command:
        try:
            interval = command[len("set interval "):]
            config.change_param(parameter="interval", value=interval)
        except Exception as e:
            send_com("Bad command", serial)
    elif "set id " in command:
        try:
            id = command[len("set id "):0]
            config.change_param(parameter="id", value=id)
        except Exception as e:
            send_com("Bad command", serial)
    elif command == "led on":
        try:
            config.change_param(parameter="led", value=True)
        except Exception as e:
            send_com("Bad command", serial)
    elif command == "led off":
        try:
            config.change_param(parameter="led", value=False)
        except Exception as e:
            send_com("Bad command", serial)
    else:
        send_com("Bad command", serial)
