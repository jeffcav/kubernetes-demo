# kubernetes-demo

## 1. Requirements

Download vagrant and virtualbox: https://www.vagrantup.com/downloads

8GB of RAM and a processor with 4+ cores is recommended.

## 2. Provision a full-fledged Kubernetes cluster in your machine

We will use Vagrant to provision VMs that form a Kubernetes cluster, as illustrated below:

![kubernetes cluster](figs/k8s-cluster.png)

Go to the `cluster/` directory, and:

1. Run `vagrant up` to create VMs
2. Run `vagrant halt` or `vagrant up` to turn off and on VMs after creation
3. Run `vagrant ssh VM-NAME` to run commands inside of a VM

## 3. Build applications containers

This demo contains one application composed of 2 services:

- **Time backend:** a time server which returns the current time.
- **Time frontend:** a web page which exhibits current time fetched from the backend.

Next sections will guide you through the build and execution of both containerized services.

## 3.1. Build docker images

To build the backend docker image, run:

```bash
cd src/python/backend
docker build -t jrac/time-backend:v1 .
cd -
```

To build the frontend docker image, run:

```bash
cd src/python/frontend
docker build -t jrac/time-frontend:v1 .
cd -
```

## 3.2. Run docker images

To start the **backend**, run:

```bash
docker run -d --rm --name backend -p 5001:5000 jrac/time-backend:v1
```

To start the **frontend**, run:

```bash
docker run -d --rm --name frontend --env TIME_SERVER=172.17.0.2:5000 -p 5000:5000 jrac/time-frontend:v1
```

Note that the frontend can be accessed via port 5000 of your host.
Type `http://localhost:5000` in your browser and you'll see the web page.

## 4. Run services in the Kubernetes cluster

Now let's use Kubernetes to orchestrate the deployment of our application composed of 2 services.

Time Backend was implemented as a Kubernetes Deployment with 3 replicas of a time server, plus a Kubernetes Service so it gets exposed to other services inside our cluster.

Time Frontend was implemented as a Kubernetes Pod that runs a web server, plus a Kubernetes Service that exposed it to outside the cluster.

### 4.1. Deploy the backend

kubectl apply -f <https://raw.githubusercontent.com/jeffcav/kubernetes-demo/main/src/k8s/backend/deployment.yaml>

kubectl apply -f <https://raw.githubusercontent.com/jeffcav/kubernetes-demo/main/src/k8s/backend/service.yaml>

### 4.2. Deploy the frontend

kubectl apply -f <https://raw.githubusercontent.com/jeffcav/kubernetes-demo/main/src/k8s/frontend/pod.yaml>

kubectl apply -f <https://raw.githubusercontent.com/jeffcav/kubernetes-demo/main/src/k8s/frontend/service.yaml>

## 5. Access application from your host

Now that all services of our application are running, we can access it performing a HTTP GET to port 30008 of any node that composes our cluster.

However, we might want to access the application we just provisioned from a browser in our host.

To do so, expose port 30008 of any VM of the cluster to the host as below.
Here we expose port 30008 as port 5050 of our host:

From the cluster/ directory of this repository, run:

`vagrant ssh k8s-node-1 -- -L 5050:localhost:30008`

Now, from a web browser in your host access: `localhost:5050` and Voilà.
