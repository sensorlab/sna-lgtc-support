FROM arm32v7/debian:jessie

# File Author / Maintainer
MAINTAINER Matevz Vucnik

# Set debian frontend
ENV DEBIAN_FRONTEND=noninteractive

# Install common dependences
RUN apt-get update --fix-missing
RUN apt-get upgrade -y
RUN apt-get install -y apt-utils
RUN apt-get install -y git

# Install dependences for vena drivers
RUN apt-get install -y gcc-arm-none-eabi
RUN apt-get install -y gdb-arm-none-eabi
RUN apt-get install -y libnewlib-arm-none-eabi
RUN apt-get install -y devscripts

# Install dependences for vesna management system
RUN apt-get install -y default-jdk
RUN apt-get install -y ant
RUN apt-get install -y librxtx-java

# Compile and install OpenOCD
WORKDIR /root
RUN git clone -b sna-lgtc https://github.com/avian2/openocd.git
WORKDIR /root/openocd
RUN mk-build-deps --install -t "apt-get -y --no-install-recommends"
RUN dpkg-buildpackage -uc -b
WORKDIR /root
RUN dpkg -i openocd_0.8.0-4tomaz-bbblack-4_armhf.deb

# Cleanup
RUN apt-get clean
