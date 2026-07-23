# Kubernetes (k8s)

## Background
k8s is a container orcherstration tool
Written in Go for microservice architecture  

## Basic Components
### K8s clients
Kubeclt CLI
Web UI
Rest APIs

### Control Plane (Master) Nodes
These are compute instances that are the brains of k8s.  
Their job is to manage the cluster(s)
Control plane nodes consists of the following:
- API Server
- Scheduler
- Controller
- Etcd

### Worker Nodes
These are compute instances that handle the containers.  
Are compromised of the following:
- Kubelet
- Kube-proxy
- Container Runtime (ContainerD by default)
- Pods

### Pods
These are the smallest k8s objects.
They contain a grouping of containers that are managed together. 
Containers in the same pod share resources and communicate via localhost

#### Pod Commands

*creating a pod*
kubectl run pod-name --image=container-image \
--port=1234 --env="KEY=VALUE" --labels="ENV=dev"

*creating a pod spec file from a command*
kubectl run nginx --image=nginx \
--dry-run-client -o yaml > nginx.yaml

*create a pod from a manifest/config file* 
kubectl apply -f nginx.yaml

*delete resources declaritively*
kubectl delete -f nginx.yaml

