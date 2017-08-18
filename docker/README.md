This is the [Installation manual](https://docs.docker.com/engine/installation/linux/docker-ce/debian) and usage instructions for the Docker daemon on ARM.

* Uninstall old versions

      $ sudo apt-get remove docker docker-engine docker.io

* Add Docker’s official GPG key:

      $ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

* Add docker repository.

      $ echo "deb [arch=armhf] https://download.docker.com/linux/debian \
        $(lsb_release -cs) stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list

* Update the apt package index.

      $ sudo apt-get update

* Install the latest version of Docker CE.

      $ sudo apt-get install docker-ce

* Create the docker group.

      $ sudo groupadd docker

* Add your user to the docker group.

      $ sudo usermod -aG docker $USER
 
* DNS setup with JSI DNS servers for docker daemon: Place the following line to `/etc/docker/daemon.json`:

      {"dns": ["193.2.4.247", "193.2.4.248"]}

* To store big Docker files somewhere else than `/var/lib/docker`, add the
  following to `/etc/docker/daemon.json`:

      {
          <any other settings, like dns>
          "graph": "<path>"
      }

  Here, `<path>` is path to a root-owned directory, usually on a mounted SD card.

* Use serial device from docker container:

      $ docker run --device=/dev/ttyS1 ...
