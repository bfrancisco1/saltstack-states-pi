copy readtemp:
  file.recurse:
    - name: /home/pi/scripts/readtemp.py
    - template: jinja
    - source: salt://temp-probe/scripts/readtemp.py