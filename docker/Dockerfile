# hadolint/hadolint
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends \
    # install firefox
    firefox \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
    libegl-dev \
    libpci-dev \
    # install a lightweight window manager
    fluxbox \
    eterm \
    # install pip
    python3-pip \
    # install xvfb/pyvirtualdisplay packages
    xvfb \
    xserver-xephyr \
    tigervnc-standalone-server \
    x11-utils \
    gnumeric \
    # install vnc server for remote access
    x11vnc \
    # tkinter is necessary to get the mouse position with pyautogui
    python3-dev \
    python3-tk \
    # necessary to take screenshots with pyautogui
    scrot \
    # clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir pip==20.0.2
COPY requirements.txt /tmp/
RUN pip install --default-timeout=15000 --no-cache-dir -r /tmp/requirements.txt

