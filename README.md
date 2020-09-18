# PhArt – The Photo Art App

1. Takes a photo
2. Converts it into paths
3. Draw it with a plotter

## network

```shell
nmap -sP 192.168.178.0/24
```

## connect

```shell
ssh pirate@black-pearl.fritz.box
# password: hypriot
docker run -d -p 80:80 hypriot/rpi-busybox-httpd
```

Open test application

```shell
open http://black-pearl.fritz.box/
```

## build

```shell
docker build -t phart .
```

apt install -y git python3 pigpiod libatlas3-base  libgfortran5 libatlas3-base libgfortran5  libilmbase-dev  libopenexr-dev libgstreamer1.0-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test libgtk-3-0 libjasper-dev

pip3 install numpy opencv-python==3.4.11.41 pigpio pillow pytest readchar tqdm
