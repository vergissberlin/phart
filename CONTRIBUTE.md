
# Contribute

If you like to make changes, feel free to do it. Just checkout the repository and build your own Docker image.

## Build & push

Beware, you have be on an ARM system, or using a [ARM simulation](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/) to build the Docker image.

```shell
docker build -t vergissberlin/phart .
docker push vergissberlin/phart
```

---

```shell
sudo apt update
sudo apt install -y git fail2ban python3 python3-pip pigpiod libatlas3-base libgfortran5 libilmbase-dev libopenexr-dev libgstreamer1.0-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test libgtk-3-0 libjasper-dev

pip3 install numpy opencv-python==3.4.11.41 pigpio pillow pytest readchar tqdm
````

### Telegraf

```shell
sudo apt install -y apt-transport-https wget
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/os-release
test $VERSION_ID = "7" && echo "deb https://repos.influxdata.com/debian wheezy stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "8" && echo "deb https://repos.influxdata.com/debian jessie stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "9" && echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "10" && echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

sudo apt-get update && sudo apt-get install telegraf
sudo service telegraf start
```
