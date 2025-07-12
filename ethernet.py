import socket

def send_message(text):
    # Параметры
    interface = "eth0"  # Укажи свой сетевой интерфейс (проверь через ip link)

    # Сообщение для отправки
    message = text

    # Формируем Ethernet фрейм: dest(6) + src(6) + type(2) + payload
    eth_frame = message

    # Создаем сырой сокет
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

    # Привязываемся к интерфейсу
    sock.bind((interface, 0))

    # Отправляем фрейм
    sock.send(eth_frame)

    print("Сообщение отправлено по Ethernet.")

def make_message(text, type):

    header = "AA0B"

    version = "01"

    command ={
        "ERROR_MESSAGE" : "01",
        "OPEN_CONNECTION" : "02",
        "CLOSE_CONNECTION" : "04",
        "PING_REQ" : "06",
        "PING_CNF" : "07",
        "SEND_MESSAGE" : "09"
    }

    if len(text) == 0:
        length = 8
    else:
        length = len(text)
    
    length = length.to_bytes(1, byteorder='big', signed=True)

    CRC16 = "00"

    message = [bytes.fromhex(header), bytes.fromhex(version), bytes.fromhex(command[type]), length, bytes.fromhex(CRC16), text.encode("utf-8")]
    
    message = b''.join(message)

    return message