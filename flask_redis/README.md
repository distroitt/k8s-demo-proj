Развернуть проект можно в minikube, последовательным применением kubectl apply -f к двум Service, Deployment. 
Зайти на сайт можно через комбинацию IP:PORT, где IP - minikube ip, PORT - 30001
Чтобы установить значение в redis: curl -X POST -d "value=HelloWorld" http://IP:PORT/set/mykey, где
mykey - ключ
HelloWorld - значение
Чтобы получить значение из redis: curl http://IP:PORT/get/mykey, где
mykey - ключ
