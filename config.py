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
            return e
    
    return param