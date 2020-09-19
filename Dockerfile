FROM 2000cubits/raspbian-python

RUN apt update
RUN apt install -y \
    git \
    pigpiod \
    python3-pip \
    libatlas3-base \ 
    libgfortran5 \
    libatlas3-base \
    libilmbase-dev \ 
    libopenexr-dev \
    libgstreamer1.0-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev \
    libqtgui4 \
    libqt4-test \
    libgtk-3-0 \
    libjasper-dev &&\
    rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    gpiozero \
    numpy \
    opencv-python==3.4.4.19 \
    picamera \
    pigpio \
    pillow \
    pytest \
    readchar \
    tqdm

WORKDIR /app

COPY ./app .

ENTRYPOINT  ["phyton3", "init.py"]
