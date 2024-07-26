## Docker

first of all install docker in your local System



##To install Docker on an Ubuntu system through the command line, follow these steps:

    Update the apt package index and install packages to allow apt to use a repository over HTTPS:

///////////////////////////////
sudo apt-get update
sudo apt-get install \
  ca-certificates \
  curl \
  gnupg \
  lsb-release
/////////////////////////////

## Add Docker’s official GPG key:
///////////////////////////
sh
//////////////////////////

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
//////////////////////////


## Update the apt package index again and install the latest version of Docker Engine and containerd:

//////////////////////////
sh
/////////////////////////
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
/////////////////////////


## Verify that Docker Engine is installed correctly by running the hello-world image:

///////////////////////
sh
///////////////////////
sudo docker run hello-world
////////////////////////
