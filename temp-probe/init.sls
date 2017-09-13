copy readtemp:
  file:
    - name: /home/pi/readtemp.py
    - template: jinja
    - source: salt://temp-probe/scripts/readtemp.py