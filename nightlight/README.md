# Nightlight

- Connect PIR sensor to PI (Pins: power, ground, data).
- Install python and libraries
  - `sudo apt-get install -y python3 python3-rpi.gpio python3-pip && pip3 install PyP100`
- Copy `nightlight.service` to `/etc/systemd/system/nightlight.service` and `sudo systemctl enable nightlight`
- Configure variables at the top of the script and `sudo systemctl restart`

Will detect motion and turn on the Tapo P100
