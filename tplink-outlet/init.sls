copy tplink-smartplug:
  file.managed:
    - name:  /opt/scripts/tplink/tplink-smartplug.py
    - makedirs:  True
    - source:  salt://tplink-outlet/scripts/tplink-smartplug.py