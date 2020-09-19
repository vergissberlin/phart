FROM 2000cubits/raspbian-python

RUN apt-get update
# RUN apt-get upgrade 
RUN apt-get install -y \
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
    numpy \
    opencv-python==3.4.4.19 \
    pibrella \
    pigpio \
    pillow \
    pytest \
    readchar \
    tqdm

WORKDIR /app

RUN git clone https://github.com/MakeMagazinDE/BrachioGraph.git .

CMD ["bash"]
