import json


def get_param():
    
    with open("config.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
        try:
            param = {
                "interval" : data['interval'],
                "id": data['id'],
                "led" : data['led'],
                "baudrate" : data['baudrate']
            }
        
        except Exception as e:
            print(f"Ошибка: {e}")
    
    return param

def change_param(parameter, value):
    data = get_param()
    try:
        data[parameter] = value
        with open('config.json', 'w') as file:  
            json.dump(data, file)
    
    except Exception as e:
        print(f"Ошибка: {e}")