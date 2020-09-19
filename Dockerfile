FROM 2000cubits/raspbian-python

RUN apt-get update
RUN apt-get install -y \
    git \
    pigpiod \
    python3-pip
RUN apt-get install -y \
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

CMD  ["python3", "phart.py"]
