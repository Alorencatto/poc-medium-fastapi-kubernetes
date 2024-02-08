# Kubernetes

## Minikube
```shell
minikube start --mount-string "$HOME/minikube/postgres-data:/data" --driver=docker --install-addons=true --kubernetes-version=stable
minikube stop
minikube delete

kubectl get nodes
```

## K3s
```shell
multipass launch --name k3s --mem 4G --disk 40G
multipass info k3s

multipass shell k3s
curl -sfL https://get.k3s.io | sh -
```

## Kind
```shell
brew install kind

kind create cluster
kind get clusters

- Pausing cluster
docker stop kind-control-plane

- Resume cluster 
docker start kind-control-plane
```

## Enable metrics on cluster
```shell
kubectl apply -f cluster/components.yml

kubectl get deployment metrics-server -n kube-system

kubectl top node
```

## Building image
```shell
docker build -t alorencatto/poc-medium-fastapi-kubernetes .
docker push alorencatto/poc-medium-fastapi-kubernetes
```

## Applying manifests
```shell
kubectl apply -f namespace/ns.yml

-- Application
kubectl apply -f code/secret.yml -n poc
kubectl apply -f code/deployment.yml -n poc
kubectl apply -f code/nodeport-service.yml -n poc
kubectl apply -f hpa/app-hpa.yml -n poc

-- Postgres
kubectl apply -f postgres/pv.yml -n poc
kubectl apply -f postgres/secret.yml -n poc
kubectl apply -f postgres/pvc.yml -n poc
kubectl apply -f postgres/deployment.yml -n poc
kubectl apply -f postgres/service.yml -n poc

-- Migration Job
kubectl apply -f job/migration.yml -n poc

-- Nginx
kubectl apply -f nginx/nginx-config.yml -n poc
kubectl apply -f nginx/nginx-deployment.yml -n poc
kubectl apply -f nginx/nginx-service.yml -n poc

-- Get resources
kubectl get deployments -n poc
kubectl get pods -n poc

kubectl get svc -n poc
kubectl get pv -n poc
kubectl get pvc -n poc
kubectl get secrets -n poc

kubectl get jobs -n poc
kubectl get hpa -n poc

kubectl describe service nginx-service -n poc
kubectl describe deployment postgres-deployment -n poc
kubectl describe pv postgres-pv -n poc

kubectl top pod -n poc

-- Exposing services
kubectl port-forward service/svc-nodeport-poc-medium-fastapi-deployment --address 0.0.0.0 8000:8000 -n poc

-- Rollout restart
kubectl apply -f code/deployment.yml -n poc
kubectl rollout restart deployment fiap-postech-selfservice-fastfood -n poc
```

## Logging
```shell

kubectl get events --all-namespaces  --sort-by='.metadata.creationTimestamp'

kubectl fiap-postech-selfservice-fastfood-84f4fcb59-j4fkf -n poc
kubectl logs fiap-postech-selfservice-fastfood-nginx-deployment-55d6d96n7h6m -n poc
kubectl logs postgres-deployment-857594b99c-tq8kn -n poc
kubectl logs fiap-postech-selfservice-fastfood-migrations-7kkg5 -n poc
```

## Housekeeping
```shell
kubectl delete -f namespace/ns.yml

kubectl delete -f code/secret.yml -n poc
kubectl delete -f code/deployment.yml -n poc
kubectl delete -f code/nodeport-service.yml -n poc
kubectl delete -f hpa/app-hpa.yml -n poc

kubectl delete -f job/migration.yml -n poc

kubectl delete -f postgres/pv.yml -n poc
kubectl delete -f postgres/secret.yml -n poc
kubectl delete -f postgres/deployment.yml -n poc
kubectl delete -f postgres/pvc.yml -n poc
kubectl delete -f postgres/service.yml -n poc

kubectl delete -f nginx/nginx-config.yml -n poc
kubectl delete -f nginx/nginx-deployment.yml -n poc
kubectl delete -f nginx/nginx-service.yml -n poc
```

## Stress test
```shell
k6 run scripts/stress-test/test-api.js

kubectl describe deployment poc-medium-fastapi-deployment -n poc
```