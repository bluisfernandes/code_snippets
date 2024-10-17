# Steps for Setting Up and Managing a Docker

## Installing on Ubuntu

1. Uninstall old versions
    ```bash
    for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
    ```

1. Set up Docker's `apt` repository.
    ```bash
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```
    > **_NOTE:_**  If you use an Ubuntu derivative distro, such as Linux Mint, you may need to use `UBUNTU_CODENAME` instead of `VERSION_CODENAME`.


1. Install the Docker packages
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

1. Verify that Docekr Engine installation is successful by running the `hello-world` image.

    ```bash
    sudo docker run hello-world
    ```

## Linux Post install

1. Create the `docker` group.
    ```bash
    sudo groupadd docker
    ```

1. Add your user to the `docker` group
    ```bash
    sudo usermod -aG docker $USER
    ```

1. Log out and log back in so that your group membership is re-evaluated.
    > If you're running Linux in a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

    You can also run the following command to activate the changes to groups:
    ```bash
    newgrp docker
    ```

1. verify that you can run `docker` commands without `sudo`
    ```bash
    docker run hello-world
    ```
