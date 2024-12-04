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
6. Desplegar Kong aplicant els helm charts: https://github.com/bitnami/charts/blob/main/bitnami/kong/values.yaml
7. Configurar les rutes, serveis necessaris per accedir al rest-server.
8. Crear usuari amb credencial( p.e.  apikey: c182cca8a7c1cc3659369fdba0bc3f27a74c804fc8ebf738dd2ad9ba76a78c73) i activar plugins per customitzar el consum que pot fer dels serveis (key-auth, rate-limit, ip-restric, request-max-size...)
