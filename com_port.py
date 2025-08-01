import serial
import time
import config
import os
import GPIO

def init_com(port, baudrate):
    try:
        ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1,
            write_timeout=1
        )
        time.sleep(2)        
        print(f"Port {port} good.")
        return ser
    except serial.SerialException as e:
        print(f"{port}: {e}")
        return None
    except Exception as e:
        print(f"{e}")
        return None


def send_com(text, serial):
    if not serial or not serial.is_open:
        print("Port not open!")
        return False

    try:
        serial.write(text.encode('utf-8'))
        print(f"Send: {text.strip()}")
        return True
    except serial.SerialTimeoutException:
        print("Error: timeout.")
        return False
    except serial.SerialException as e:
        print(f"Error port: {e}")
        return False
    except Exception as e:
        print(f"{e}")
        return False



def command(command_text, serial):
    
    if "set interval " in command_text:
        try:
            interval = command_text[len("set interval "):]
            config.change_param(parameter="interval", value=interval)
        except Exception as e:
            send_com("Bad command\n\r", serial)
            print(f'{e}')
    elif "set id " in command_text:
        try:
            id = command_text[len("set id "):]
            config.change_param(parameter="id", value=int(id))
        except Exception as e:
            send_com("Bad command\n\r", serial)
            print(f'{e}')
    elif "set baudrate " in command_text:
        try:
            id = command_text[len("set baudrate "):]
            config.change_param(parameter="baudrate", value=int(id))
        except Exception as e:
            send_com("Bad command\n\r", serial)
            print(f'{e}')
    elif command_text == "led on":
        try:
            GPIO.led_on()
        except Exception as e:
            send_com("Bad command\n\r", serial)
            print(f'{e}')
    elif command_text == "led off":
        try:
            GPIO.led_off()
        except Exception as e:
            send_com("Bad command\n\r", serial)
            print(f'{e}')
    elif command_text == "halt":
        try:
            os.system("sudo shutdown now")
        except Exception as e:
            send_com("Bad command\n\r", serial)
            print(f'{e}')
    else:
        send_com("Bad command\n\r", serial)

def listen_com(serial):
    try:
        while True:
            if serial.in_waiting > 0:
                line = serial.readline().decode('utf-8', errors='ignore').strip()
                if line:
                    command(line, serial)
            time.sleep(0.01)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    BAUDRATE = 9600
    PORT = '/dev/ttyUSB0'
    ser = init_com(PORT, BAUDRATE)

    if not ser:
        print("Cant open port")
        exit(1)
    try:
        listen_com(serial=ser)
    except KeyboardInterrupt:
        print("\nUser kill")
    finally:
        ser.close()
        print("Port close")
