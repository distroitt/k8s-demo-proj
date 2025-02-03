Развернуть проект можно в minikube, последовательным применением kubectl apply -f к pv.yaml, pvc.yaml, service, deployment. Зайти на сайт можно через комбинацию IP:PORT, где IP - minikube ip, PORT - 30001 
Чтобы установить значение в доске сообзений: curl -X POST -d '{"message": "Hello World"}' -H "Content-Type: application/json" http://IP:PORT/messages 
Чтобы получить значения с доски сообщение: curl http://IP:PORT/messages
