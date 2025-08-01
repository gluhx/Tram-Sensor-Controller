import time
import threading
import gps
import config
import com_port as COM
import GPIO

parameters = config.get_param()
GPIO.init_GPIO(18)
BAUDRATE = parameters['baudrate']
PORT = '/dev/ttyUSB0'
serial = COM.init_com(PORT, BAUDRATE)

def write():
    while True:
        #получаем параметры для работы
        parameters = config.get_param()
        try:
            try:
                #получаем данные gps
                data = gps.get_data()

                #составляем из данных сообщение
                text_message = str(parameters['id']) + ';' + data["date"] + "," + data["time"] + ";" + data["longtitude"] + "," + data["latitude"] + ";" + data["height"] + '\n\r'
            except Exception as e:
                text_message = str(parameters['id']) + ';' + "No data from GPS\n\r"
            #отравляем сообщение на COM
            if not serial:
                print("Cant open port")
                exit(1)
            COM.send_com(text=text_message, serial=serial)

            #делаем задержку
            time.sleep(parameters['interval'])

        except KeyboardInterrupt:
            print("Пользователь закончил выполнение программы.")


def reading():
    while True:
        if not serial:
            print("Cant open port")
            exit(1)
        COM.listen_com(serial=serial)



# Запуск потоков
if __name__ == "__main__":
    t1 = threading.Thread(target=write, daemon=True)
    t2 = threading.Thread(target=reading, daemon=True)

    t1.start()
    t2.start()

    try:
        # Основной поток ждёт, пока не нажмём Ctrl+C
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Завершение...")
