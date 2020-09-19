# PhArt – The Photo Art App

1. Takes a photo
2. Converts it into paths
3. Draw it with a plotter

## Installation

### Raspberry PI with Docker

- If you not allready installed Docker on your raspberry pi os of your your choice I suggest to download the [hypriot os for raspberry pi](https://blog.hypriot.com/downloads/) and follow the instructions. It is based on raspbian and comes with Docker preinstalled.
- Use the [belana etcher](https://www.balena.io/etcher/) or the command line too `df` to burn the image on a SD card as described.
- Put the SD card in you RPI and connect it to your network with a LAN cable.

### Network

- Scan your network and find out on which IP your RPI is adressed. You can also use app like [fing](https://www.fing.com/) on your mobile.

```shell
nmap -sP 192.168.1.0/24
```

### Connect

- If you have a fritzbox with DNS activated, your should be ablue to use the hostname to connect to your RPI. The address is like so black-pearl.fritz.box otherwise you have to take the IP address.

```shell
ssh pirate@black-pearl.fritz.box # password: hypriot
```

#### Test application

```shell
docker run -d -p 80:80 hypriot/rpi-busybox-httpd
open http://black-pearl.fritz.box/
```

You can see a test application in your browser? Than you`re good to go, if not go back to _start_ without getting 400 € from the bank.

#### Start PhArt

```shell
docker run -d --restart unless-stopped --privileged --name phart vergissberlin/phart
```

#### Debug

```shell
docker exec phart bash
```

## Contribute

If you like to make changes, feel free to do it. Just checkout the repository and build your own Docker image.

### Build

```shell
docker build -t vergissberlin/phart .
```

---

apt install -y git python3 pigpiod libatlas3-base libgfortran5 libatlas3-base libgfortran5 libilmbase-dev libopenexr-dev libgstreamer1.0-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test libgtk-3-0 libjasper-dev

pip3 install numpy opencv-python==3.4.11.41 pigpio pillow pytest readchar tqdm
