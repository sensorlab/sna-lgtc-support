# Running Docker

Dockerfiles in this directory are used to build a `vesna-tools` image that
contains development tools for compiling and programming firmware for the guest
VESNA SNC board from inside a Docker container.

The `vesna-tools` is a multi-architecture Docker image. There is a `Dockerfile`
for each architecture. `amd64` is used for development of firmware on a typical
PC. `arm` is used for compiling firmware on the SNA-LGTC boards.

`vesna-tools` is not very useful on its own. It is meant to be used as a base for other
container images, such as the [VESNA management system](https://github.com/matevzv/vesna-management-system).
A simple example containerized application using `vesna-tools` is the [Logatec temperature monitor](https://github.com/avian2/logatec-temp-monitor).

Version 2 is used as a base container image for [logatec testbed experiments](https://github.com/logatec3/logatec-experiment).

The `vesna-tools` image is also available on [Docker Hub](https://hub.docker.com/r/sensorlab6/vesna-tools/).
Running `docker pull` automatically pulls the image for the current architecture.

## Installing Docker on SNA-LGTC

These instructions are based on the [Get Docker CE for Debian](https://docs.docker.com/engine/installation/linux/docker-ce/debian) section from Docker Documentation.

* Uninstall old versions

      $ sudo apt-get remove docker docker-engine docker.io

* Add Docker’s official GPG key:

      $ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

* Add Docker repository.

      $ echo "deb [arch=armhf] https://download.docker.com/linux/debian \
        $(lsb_release -cs) stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list

* Update the apt package index.

      $ sudo apt-get update

* Install the latest version of Docker CE.

      $ sudo apt-get install docker-ce

* Create the Docker group.

      $ sudo groupadd docker

* Add your user to the Docker group.

      $ sudo usermod -aG docker $USER
 
* DNS setup with JSI DNS servers for Docker daemon: Place the following line to `/etc/docker/daemon.json`:

      {"dns": ["193.2.4.247", "193.2.4.248"]}

* To store big Docker files somewhere else than `/var/lib/docker`, add the
  following to `/etc/docker/daemon.json`:

      {
          <any other settings, like dns>
          "data-root": "<path>"
      }

  Here, `<path>` is path to a root-owned directory, usually on a mounted SD card.

## Building `vesna-tools` image and pushing to Docker Hub

Build the image for each platform. For example, on the SNA-LGTC board you should
run:

    $ docker build -t sensorlab6/vesna-tools-arm -f Dockerfile.arm .
    $ docker push sensorlab6/vesna-tools-arm

On a PC, use the same commands, except replace `arm` with `amd64`.

When all architectures are built and pushed, you need to also push the manifest
list file:

    $ manifest-tool push from-spec vesna-tools.yaml

Get and compile `manifest-tool` from [this repository](https://github.com/estesp/manifest-tool) on GitHub.

## Other useful Docker commands

* Build the Dockerfile in the current directory.

      $ docker build -t some-name .

* Use GPIO pins and serial device from Docker container:

      $ docker run -v /sys/class/gpio:/sys/class/gpio --device=/dev/ttyS1 --privileged ...
    
* Delete volumes

      $ docker volume ls 
      $ docker volume rm $(docker volume ls -qf dangling=true)

* Remove docker containers

      $ docker ps
      $ docker ps -a
      $ docker rm $(docker ps -qa --no-trunc --filter "status=exited")

* Remove docker images

      $ docker images
      $ docker rmi $(docker images --filter "dangling=true" -q --no-trunc)

* Kill all running containers

      $ docker kill $(docker ps -q)
