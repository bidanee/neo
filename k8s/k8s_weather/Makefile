all: build run k8init appdep appsvc getdep getsvc getpod
restart:  delsvc deldep delpod appdep appsvc getdep getsvc getpod
stop: delsvc deldep delpod
build:
	docker build -t weathers .
run:
	docker run -it -d -p 8000:8000 --name weathers weathers
exec:
	docker exec -it weathers /bin/bash
start:
	docker start weathers
stop:
	docker stop weathers
logs:
	docker logs weathers
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)

k8init:
	docker commit weathers weathers
	docker tag weathers bidanee/weathers
	docker push bidanee/weathers
	docker rm -f $$(docker ps -aq)
	docker rmi -f $$(docker images -q)
getnode:
	kubectl get nodes
appdep:
	kubectl apply -f deployment.yaml
appsvc:
	kubectl apply -f service.yaml
getdep:
	kubectl get deployment
getsvc:
	kubectl get svc -o wide
getpod:
	kubectl get pod -o wide
delsvc:
	kubectl delete svc weathers
deldep:
	kubectl delete deployment weathers
delpod:
	kubectl get pod | grep weathers | awk '{print $$1}' | xargs -I {} kubectl delete pod {} --force
desdep:
	kubectl describe deployment weathers
dessvc:
	kubectl describe svc weathers
despod:
	kubectl describe pod weathers

