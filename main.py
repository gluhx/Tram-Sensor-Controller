import time
import gps
import ethernet as eth
import temperature as temp


while True:
    try:
        #получаем данные gps
        data = gps.get_data()

        #получаем данные с датчика температуры
        data_temp = {
            "temperature" : str(temp.get_temperature()),
            "humidity": str(temp.get_humidity())
        }

        #составляем из данных сообщение
        text_message = data["date"] + "," + data["time"] + ";" + data["longtitude"] + "," + data["latitude"] + ";" + data["height"] + ";" + data_temp["temperature"] + ";" + data_temp["humidity"]
        
        #добавляем к сообщению служебные байты
        message = eth.make_message(text_message, "SEND_MESSAGE")

        #отравляем сообщение на eth0
        eth.send_message(message)

        #делаем задержку на 10 секунд
        time.sleep(10)
    except KeyboardInterrupt:
        print("Пользователь закончил выполнение программы.")
    finally:
        print("Конец отправки")
