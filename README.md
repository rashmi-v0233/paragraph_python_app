# paragraph_python_app
My test Python App

Pre-requisite:
 -- Docker shoud be installed.

Dockerhub repo:
https://hub.docker.com/repository/docker/rashmiv0233/python_paragraph_project/general

Instructions:
(1) Build the image:
      $ docker build -t test_image .

(2) Run a container out of the image
    $ docker run -it --name test_app test_image

(3) Tag the image
    $ docker tag test_image:latest rashmiv0233/python_paragraph_project:<major version>.<minor version>

(4) Push image to dockerhub repo
    $ docker push rashmiv0233/python_paragraph_project:<major version>.<minor version>

(5) VERY IMPORTANT:
    COPY the file from container to Host
    $ docker cp <containerId>:file_with_lines.txt /host/path/target

Last funcional image on dockerhub:
https://hub.docker.com/layers/rashmiv0233/python_paragraph_project/1.0/images/sha256-a17ff58cc76c5cc3aee0715d32e5fa87853fadb281a19b0fc156d2721291b5c1?context=repo

