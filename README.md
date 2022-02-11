# kubernetes-demo

## 1. Requirements

Download vagrant and virtualbox: https://www.vagrantup.com/downloads

8GB of RAM and a processor with 4+ cores is recommended.

## 2. Provision a Kubernetes cluster

Go to the `cluster/` directory and run `vagrant up`.

Vagrant will provision 2 VMs on your machine: `k8s-master` and `node-1`, and they form a kubernetes cluster.

After their creation, to turn on and off the VMs run `vagrant up` and `vagrant off` respectively.

To run commands inside the VMs, run `vagrant ssh k8s-master` or `vagrant ssh node-1`.

These VMs will be later used to provision 2 services inside the kubernetes cluster.

## 3. Build images of applications

This demo contains one application composed of 2 services:

- Time backend: a time server which returns the current time.
- Time frontend: a web page which exhibits current time fetched from the backend.

To build docker images for both services:

- Enter the `apps/backend` directory and run `docker build -t backend:v1 .`
- Enter the `apps/frontend` directory and run `docker build -t frontend:v1 .`

Push your images to a container registry like Dockerhub.
In this demo we push them to `jrac/time-backend:v1` and `jrac/time-frontend:v1` respectively.

## 4. Run application images

To start the **backend**, run:

`docker run -d --rm --name backend -p 5001:5000 jrac/time-backend:v1`


To start the **frontend**, run:

`docker run -d --rm --name frontend --env TIME_SERVER=172.17.0.2:5000 -p 5000:5000 jrac/time-frontend:v1`

Note that the frontend can be accessed via port 5000 of your host.
Type `http://localhost:5000` in your browser and you'll see the web page.
