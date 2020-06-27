import requests
import time
import RPi.GPIO as GPIO

line_notify_token = '********************'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = '郵便物が来ました。'

GPIO.setmode(GPIO.BCM)
#GPIO18pinを入力モードとし、pull up設定とします 
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)
sw_status = 0
sw_status_1 = 0

while True:
    try:
        sw_status = GPIO.input(24)
        if sw_status == 0:
            print("Close")
            sw_status_1 = 0
            
        else:
            print("Open!")
            if sw_status_1 == 0:
              payload = {'message': message}
              headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
              line_notify = requests.post(line_notify_api, data=payload, headers=headers)  
            sw_status_1 = 1
        time.sleep(0.1)
    except:
        break





