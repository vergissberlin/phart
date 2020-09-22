FROM 2000cubits/raspbian-python

ENV LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0

RUN apt-get update 
RUN apt-get install -yq --no-install-recommends \
    git \
    python3-pip

RUN apt-get install -yq --no-install-recommends \
    libatlas3-base \ 
    libavcodec-dev \
    libavformat-dev \
    libgfortran5 \
    libgstreamer1.0-dev \
    libgtk-3-0 \
    libilmbase-dev \ 
    libjasper-dev \
    libopenexr-dev \
    libswscale-dev \
    libqt4-test \
    libqtgui4 \
    && rm -rf /var/lib/apt/lists/*

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

CMD  ["python3", "test.py"]
