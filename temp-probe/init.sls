copy readtemp:
  file.managed:
    - name: /home/pi/scripts/readtemp.py
    - template: jinja
    - makedirs: True
    - source: salt://temp-probe/scripts/readtemp.py