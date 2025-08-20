

oc  apply -f ConfigMap.yaml

----

app-docker

docker build -t mongo-crud-server .
docker tag mongo-crud-server yitzchakdamen/mongo-crud-server:v11
docker push yitzchakdamen/mongo-crud-server:v11


app-k8s

oc apply -f data_loader-deployment.yaml
oc apply -f data_loader-service.yaml
oc  expose service/mongo-crud-server-app-service

-----

mongo

oc apply -f mongo-pvs.yaml
oc apply -f mongo-deployment.yaml
oc apply -f mongo-service.yaml
