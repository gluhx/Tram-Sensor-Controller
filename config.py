import json


def get_param():
    
    with open("config.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
        try:
            param = {
                "interval" : data['interval'],
                "id": data['id'],
                "baudrate" : data['baudrate']
            }
        
        except Exception as e:
            print(f"Ошибка: {e}")
    
    return param

def change_param(parameter, value):
    data = get_param()
    try:
        if parameter == "interval":
            data[parameter] = float(value)
        else:
            data[parameter] = int(value)
        with open('config.json', 'w') as file:  
            json.dump(data, file)
    
    except Exception as e:
        print(f"Ошибка: {e}")
