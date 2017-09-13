copy readtemp:
  file.managed:
    - name: /home/pi/readtemp.py
    - template: jinja
    - source: salt://temp-probe/scripts/readtemp.py