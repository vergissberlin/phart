
# Contribute

If you like to make changes, feel free to do it. Just checkout the repository and build your own Docker image.

## Build & push

Beware, you have be on an ARM system, or using a [ARM simulation](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/) to build the Docker image.

```shell
docker build -t vergissberlin/phart .
docker push vergissberlin/phart
```

---

apt install -y git python3 pigpiod libatlas3-base libgfortran5 libilmbase-dev libopenexr-dev libgstreamer1.0-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test libgtk-3-0 libjasper-dev

pip3 install numpy opencv-python==3.4.11.41 pigpio pillow pytest readchar tqdm
