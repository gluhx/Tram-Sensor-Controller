import time
import threading
import gps
import config
import com_port as COM
import GPIO

GPIO.init_GPIO()
serial = COM.init_com()

def write():
    while True:
        #получаем параметры для работы
        parameters = config.get_param()
        try:
            #получаем данные gps
            data = gps.get_data()

            #составляем из данных сообщение
            text_message = str(parameters['id']) + ';' + data["date"] + "," + data["time"] + ";" + data["longtitude"] + "," + data["latitude"] + ";" + data["height"]

            #отравляем сообщение на eth0
            COM.send_com(text=text_message, serial=serial)

            if parameters['led']:
                GPIO.led_on()
            else:
                GPIO.led_off()

            #делаем задержку
            time.sleep(parameters['interval'])

        except KeyboardInterrupt:
            print("Пользователь закончил выполнение программы.")
        finally:
            print("Конец отправки")


def reading():
    while True:
        COM.listen_com(serial=serial, callback=COM.command)



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