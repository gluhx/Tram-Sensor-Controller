import os
import json


def send_command(command):
    os.system(command)


def init_gps():
    send_command("systemctl stop gpsd")
    send_command("systemctl start gpsd")


def get_gps_data_gpsd(file):
    
    send_command("gpspipe --json -n 4 > " + file)


def parsing_json(file):

    data_list = []

    with open(file, 'r') as text:
        for line in text:
            gps_data = str(line)
        
    gps_data = gps_data.replace("false", "False", -1)
    gps_data = gps_data.replace("true", "True", -1)

    return eval(gps_data)

def get_gps_data_dict(dict):
    gps_data = {
        "latitude" : str(dict["lat"]),
        "longtitude" : str(dict["lon"]),
        "height" : str(round(int(dict["altMSL"]), 0)),
        "date" : str(dict["time"][:10]),
        "time" : str(dict["time"][11:19])
    }

    if len(gps_data["latitude"]) < 10:
        gps_data["latitude"] += "0"*(10 - len(gps_data["latitude"]))
    
    if len(gps_data["longtitude"]) < 10:
        gps_data["longtitude"] += "0"*(10 - len(gps_data["longtitude"]))

    return gps_data

def get_data():

    filename = "gps_log.json"
    get_gps_data_gpsd(filename)
    dict = parsing_json(filename)
    data = get_gps_data_dict(dict)

    send_command("rm " + filename)

    return data

