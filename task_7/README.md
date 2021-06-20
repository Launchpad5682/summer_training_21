# Docker Web App - Platform as a Service 🐳🐳

## Description

This is the Web App providing Docker container as a service(i.e. Platform as a service). This Web App supports the following container commands and all the Linux commands:
- docker images
- docker ps
- docker run
- docker rm -f
- docker exec

 <hr>

## Dependencies
- python cgi
- apache webserver
- python subprocess

<hr>

## Setup
- This project is hosted on different server(frontend and backend on different servers). So, we need to enable the CORS in the header.
- Then, place the frontend code in `/var/www/html/` and backend code in `/var/www/cgi-bin/`.
- Enable SELinux for the `cgi-bin` and `docker`, they must be in same context or just use `setenforce 0` while testing and add the `apache` user to `/etc/sudoers` file for running docker containers. 

<hr>

## Demo 
[![Demo Video](https://i9.ytimg.com/vi_webp/wDcCXo9zyI0/mqdefault.webp?sqp=CKyZvoYG&rs=AOn4CLBGVlQwqZAH7cwmUZdclVXOagM_Ug)](https://youtu.be/wDcCXo9zyI0)

<hr>

## Future Work
- UI/UX can be improved. 
- Security can be improved.
- Add functionality like online compilers or IDEs.