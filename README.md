# **PhArt** – The **Ph**oto to **Art** App

[![Build Status](https://travis-ci.com/vergissberlin/phart.svg?branch=master)](https://travis-ci.com/vergissberlin/phart)

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

---

## Hardware assembling

### Hardware requirements

1. Raspberry PI (minimum rpi B+)
2. SD card (minimum 8GB capacity)
3. 3 9g servos
4. 3d printer with filament
5. Wires
6. A pen
7. 3 \* colourful 3.3v LEDs with 200ohm resitors for the status
8. 4 \* bright 3.3v LEDs with 50ohm resitors for the flash light
9. RaspberryPI camera module
10. Micro USB power supply

## Software Installation

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

If you like to have a bin more fancy, you can use _docker-compose_ too:

```yaml
version: '3.5'

services:
  phart:
    image: vergissberlin/phart
    container_name: phart
    privileged: true
    environment:
      - PIN_LIGHT_GREEN=4
      - PIN_LIGHT_YELLOW=17
      - PIN_LIGHT_RED=21
      - PIN_INPUT_A=9
      - PIN_INPUT_B=7
      - PIN_INPUT_C=8
      - PIN_INPUT_D=10
      - PIN_OUTPUT_A=22
      - PIN_OUTPUT_B=23
      - PIN_OUTPUT_C=24
      - PIN_OUTPUT_D=25
      - PIN_BUTTON=11
      - PIN_BUZZER=18
    volumes:
      - ./data/images:/app/images
    restart: unless-stopped
```

#### Debug

```shell
docker exec phart bash
```
