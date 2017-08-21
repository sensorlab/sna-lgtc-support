FROM arm32v7/debian:jessie

# File Author / Maintainer
MAINTAINER Matevz Vucnik

# Set debian frontend
ENV DEBIAN_FRONTEND=noninteractive

# Install common dependences
RUN	apt-get update --fix-missing
RUN	apt-get upgrade -y
RUN	apt-get install -y apt-utils git && \
	apt-get clean -y

# Install dependences for vena drivers
RUN 	apt-get install -y	gcc-arm-none-eabi \
				gdb-arm-none-eabi \
				libnewlib-arm-none-eabi \
				devscripts && \
	apt-get clean -y

# Install dependences for vesna management system
RUN	apt-get install -y	default-jdk \
				ant \
				librxtx-java && \
	apt-get clean -y

# Compile and install OpenOCD
WORKDIR /root

RUN	git clone -b sna-lgtc https://github.com/avian2/openocd.git && \
	cd openocd && \
	mk-build-deps --install -t "apt-get -y --no-install-recommends" && \
	dpkg-buildpackage -uc -b && \
	cd .. && \
	dpkg -i openocd_*.deb && \
	apt-get clean && \
	apt-get remove -y openocd-build-deps && \
	apt-get autoremove -y && \
	rm -rf openocd && \
	rm -f openocd_*.deb openocd_*.changes
