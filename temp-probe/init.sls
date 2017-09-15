copy readtemp:
  file.managed:
    - name: /home/pi/scripts/readtemp.py
    - template: jinja
    - makedirs: True
    - source: salt://temp-probe/scripts/readtemp.py

copy deviceclient:
  file.managed:
    - name: /home/pi/scripts/DeviceClient.py
    - source: salt://temp-probe/scripts/DeviceClient.py

copy passfailled:
  file.managed:
    - name: /home/pi/scripts/passfailled.py
    - source: salt://temp-probe/scripts/passfailled.py