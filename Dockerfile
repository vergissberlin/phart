FROM balenalib/rpi-raspbian:latest 
# FROM balenalib/raspberrypi3-python:3.8-build
# balenalib/raspberrypi3-python:3.7
# balenalib/raspberry-pi-python:3.7
# balenalib/raspberry-pi2-python:3.7
# balenalib/rpi-raspbian (rpi base image)
# https://stackoverflow.com/questions/54842833/access-raspistill-pi-camera-inside-a-docker-container

RUN install_packages \
    git \
    python3 \
    python3-pip \
    raspi-config

RUN install_packages \
    libatlas3-base \ 
    libavcodec-dev \
    libavformat-dev \
    libgfortran5 \
    libgstreamer1.0-dev \
    libgtk-3-0 \
    libilmbase-dev \ 
    libjasper-dev \
    libopenexr-dev \
    libraspberrypi-bin \
    libswscale-dev \
    libqt4-test \
    libqtgui4

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0 \
ENV LD_LIBRARY_PATH=/opt/vc/lib \
    UDEV=1

ADD ./app/ .
ADD /rootfs/boot/config.txt /boot/config.txt
ADD /rootfs/etc/udev/rules.d/99-camera.rules /etc/udev/rules.d/99-camera.rules

CMD  ["python3", "test.py"]
