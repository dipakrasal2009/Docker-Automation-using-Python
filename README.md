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
///////////////////////



## This is docker automation project

## 🖥️🖥️ Introducing My Latest Project of Docker Automation : Docker Image Launcher 🖥️🖥️

I'm thrilled to share my latest project: a web interface for managing Docker images! This tool allows users to download, run, and stop Docker images, all through an intuitive and user-friendly interface. Plus, it features an interactive terminal to monitor and interact with running containers in real-time.

## 🌟 Key Features:
Download Docker Images: Simply enter the image name and download it directly.
Run Docker Images: Seamlessly start the downloaded images with ease.
Stop Docker Images: Stop running Docker images with a single click.
Interactive Terminal: Real-time terminal emulation to interact with running containers.

## 🔧 Technologies Used:
Frontend: HTML, CSS, JavaScript
Github Link of the FrontEnd code : https://lnkd.in/dxBTdcnX

## Backend: Flask (Python)
Github Link of the BackEnd Code : https://lnkd.in/d-T5KW5d

## Infrastructure: AWS EC2
Real-Time Communication: Flask-SocketIO and xterm.js

## 📜 Project Overview:
User Input: The interface takes the Docker image name as input.
Download Image: A GET request is made to a Flask endpoint to pull the specified Docker image.
Run Image: A POST request starts the Docker container, and the container ID is returned.
Stop Image: Another POST request stops the running container based on the image name.
Interactive Terminal: WebSockets are used to connect to the running container, and xterm.js is used to display the terminal in the browser.

## 🖥️ How It Works:

## Frontend:
Users enter the Docker image name.
Buttons trigger JavaScript functions to send HTTP requests to the backend.
The interactive terminal is implemented using xterm.js, providing a real-time view of the container's terminal.

## Backend:
Flask handles the HTTP requests for pulling, running, and stopping Docker images.
Flask-SocketIO manages WebSocket connections for real-time communication between the server and the client.
Docker commands are executed using Python's subprocess module.

## Infrastructure:
The application is hosted on an AWS EC2 instance, ensuring reliable performance and scalability.
This project combines several technologies to create a seamless and efficient Docker management experience. I'm excited to continue improving this tool and adding more features in the future!

