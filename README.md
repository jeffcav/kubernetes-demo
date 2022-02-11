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

## 3. Containerize our services

This demo contains one application composed of 2 services:

- Time backend: a time server which returns the current time.
- Time frontend: a web page which exhibits current time fetched from the backend.

Next sections will guide you through the build and execution of both containerized services.

## 3.1. Build docker images

To build docker images for both services:

- Enter the `apps/backend` directory and run `docker build -t backend:v1 .`
- Enter the `apps/frontend` directory and run `docker build -t frontend:v1 .`

Push your images to a container registry like Dockerhub.
In this demo we push them to `jrac/time-backend:v1` and `jrac/time-frontend:v1` respectively.

## 3.2. Run docker images

To start the **backend**, run:

`docker run -d --rm --name backend -p 5001:5000 jrac/time-backend:v1`


To start the **frontend**, run:

`docker run -d --rm --name frontend --env TIME_SERVER=172.17.0.2:5000 -p 5000:5000 jrac/time-frontend:v1`

Note that the frontend can be accessed via port 5000 of your host.
Type `http://localhost:5000` in your browser and you'll see the web page.

## 4. Run services in the Kubernetes cluster

Now let's use Kubernetes to orchestrate the deployment of our application composed of 2 services.

Time Backend was implemented as a Kubernetes Deployment with 3 replicas of a time server, plus a Kubernetes Service so it gets exposed to other services inside our cluster.

Time Frontend was implemented as a Kubernetes Pod that runs a web server, plus a Kubernetes Service that exposed it to outside the cluster.

### 4.1. Deploy the backend

kubectl apply -f <https://raw.githubusercontent.com/jeffcav/kubernetes-demo/main/k8s/backend/deployment.yaml>

kubectl apply -f <https://raw.githubusercontent.com/jeffcav/kubernetes-demo/main/k8s/backend/service.yaml>

### 4.2. Deploy the frontend

kubectl apply -f <https://raw.githubusercontent.com/jeffcav/kubernetes-demo/main/k8s/frontend/pod.yaml>

kubectl apply -f <https://raw.githubusercontent.com/jeffcav/kubernetes-demo/main/k8s/frontend/service.yaml>

## 5. Access application from your host

Now that all services of our application are running, we can access it performing a HTTP GET to port 30008 of any node that composes our cluster.

However, we might want to access the application we just provisioned from a browser in our host.

To do so, expose port 30008 of any VM of the cluster to the host as below.
Here we expose port 30008 as port 5050 of our host:

From the cluster/ directory of this repository, run:

`vagrant ssh node-1 -- -L 5050:localhost:30008`

Now, from a web browser in your host access: `localhost:5050` and Voilà.
