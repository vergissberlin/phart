# PhArt – The Photo Art App

## Hardware

1. Raspberry PI (min b+)
2. 3 9g servos
3. 3d printer with filament
4. Wires
5. A pen
6. 3 * 3.3v LED
7. 3 * 200ohm resitors
8. RaspberryPI camera module

## Process

When you have finished assembling the hardware, you can start the machine, and if everything is in order, the following will happen:

1. **Photo**
   1. Pulse() RED light
   2. Blink flash light 3 times short
   3. Take a photo with long flash light
   4. Turn off flash light
   5. Solid RED light
2. **Converting**
   1. Pulse() YELLOW light
   2. Convert it into paths
   3. Solid YELLOW light
3. **Draw it**
   1. Pulse() GREEN light
   2. Draw it with the plotter
   3. Solid GREEN light

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

### Build & push

Beware, you have be on an ARM system, or using a [ARM simulation](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/) to build the Docker image.

```shell
docker build -t vergissberlin/phart .
docker push vergissberlin/phart
```

---

apt install -y git python3 pigpiod libatlas3-base libgfortran5 libilmbase-dev libopenexr-dev libgstreamer1.0-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test libgtk-3-0 libjasper-dev

pip3 install numpy opencv-python==3.4.11.41 pigpio pillow pytest readchar tqdm
