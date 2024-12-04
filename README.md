# Kong Gateway amb Rest server

Aquesta és una aplicació API REST que respon a les següents crides:

1. GET /date: retorna la data segons l'hora del pod.
2. POST /store: retorna el missatge d'haver desat les dades passades al body de la crida.

## Requisits previs

1. **Docker i Docker Compose o Kind/Minikube**: L'aplicació s'executa en contenidors Docker.
2. **Git**: Per descarregar el repositori.

---
## Instal·lació i posada en marxa
1. Crear un cluster de K8s (kind create cluster --config cluster-config.yaml)
2. Instal·lar l'Ingress controller Nginx (4 passos) https://medium.com/@dikkumburage/how-to-install-nginx-ingress-controller-93a375e8edde
3. Aplicar els manifests de la carpeta manifests (deployment, service i ingress)
4. Modificar l'/etc/hosts amb IP-cluster rest-server.local
5. Comprovar l'accés al servei ofert per pod: 
    1. curl -X GET http://rest-server.local/date // {"date":"2024-12-04 09:32:15"}
    2. curl -X POST http://rest-server.local/store -H "Content-Type: application/json" -d '{"a":1}' // "message": "Data received and stored: {'a': 1}"
