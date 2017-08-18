This is the configuration and usage instructions for the Docker daemon on BeagleBone.

 * [Instalation instructions](https://docs.docker.com/engine/installation/linux/docker-ce/debian) for Docker on ARM.
 
 * DNS setup with JSI DNS servers for docker daemon: Place the following line to `/etc/docker/daemon.json`:

    `{"dns": ["193.2.4.247", "193.2.4.248"]}`

 * To store big Docker files somewhere else than `/var/lib/docker`, add the
   following to `/etc/docker/daemon.json`:

       {
           <any other settings, like dns>
           "graph": "<path>"
       }

   Here, `<path>` is path to a root-owned directory, usually on a mounted SD card.

 * Use serial device from docker container:

    `docker run --device=/dev/ttyS1 ...`
