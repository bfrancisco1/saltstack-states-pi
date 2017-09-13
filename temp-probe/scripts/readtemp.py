{% for device, args in pillar['temp-probes'].iteritems() %}

import os
import glob
import time
import calendar
import time
import DeviceClient
import sys
import json
import passfailled as pf
import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

print(str(calendar.timegm(time.gmtime())) + ',' + str(read_temp()))

Azure_DeviceName = {{ device }}
Azure_DeviceKey = '4X/AKBYw7o88R+uekSwSawuGykFQnGOU9mQbpf8WUFE='
Azure_IoTHubName = 'BF-Test-IOT'

t = str(read_temp())

Json_Message = {'deviceid' : Azure_DeviceName, 'temperature' : t}

print(Json_Message)
Encoded_Message = json.dumps(Json_Message).encode('utf8')
Device = DeviceClient.DeviceClient(Azure_IoTHubName.lower(), Azure_DeviceName, Azure_DeviceKey)
Device.create_sas(600)
Azure_Sender = Device.send(Encoded_Message)
print(Azure_Sender)
if Azure_Sender == 204:
  print('Success')
  pf.greenOn()
  time.sleep(5)
  pf.greenOff()
  GPIO.cleanup()
else:
  print('Failure')
  pf.redOn()
  time.sleep(5)
  pf.redOff()
  GPIO.cleanup()
