import schedule
import json
import requests
from pathlib import Path
from sys import platform


def check_api():
    pass

schedule.every().hour.do(check_api)

def op_system():
    path = Path()

    request = requests.get("https://kztimerglobal.com/api/v1.0/maps?is_validated=true")
    request_text = request.text
    info = json.loads(request_text)
    
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        for file in path.glob('maps/*.bsp'):
            print(file)
    elif platform == "win32":
        for file in path.glob(r'maps\*.bsp'): # has to be a raw string otherwise it'll give an anomalous backslash error
            print(file)