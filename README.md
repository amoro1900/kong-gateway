# Kong Gateway amb Rest server

Aquesta és una aplicació API REST que respon a les següents crides:

1. GET /date: retorna la data segons l'hora del pod.
2. POST /store: retorna el missatge d'haver desat les dades passades al body de la crida.

## Requisits previs

1. **Docker i Docker Compose o Kind/Minikube**: L'aplicació s'executa en contenidors Docker.
2. **Git**: Per descarregar el repositori.

---
## Instal·lació i posada en marxa
1. Crear un cluster de K8s amb Minikube. Gui instal3lació minikube a https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download
2. Instal·lar l'Ingress controller d'Nginx https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/
3. Aplicar els manifests de la carpeta manifests (deployment, service i ingress). El pod rest-server-xxxxxxx s'haurà creat juntament amb el sevei i ingress
4. Obtenir la ip del container docker que executa minikube (docker inspect nom-container). Modificar l'/etc/hosts afegint una nova línia amb 'ip-container-minikube   rest-server.cat'
5. Comprovar l'accés al servei ofert per pod: 
    1. curl -X GET http://rest-server.cat/date // {"date":"2024-12-04 09:32:15"}
    2. curl -X POST http://rest-server.cat/store -H "Content-Type: application/json" -d '{"a":1}' // "message": "Data received and stored: {'a': 1}"
6. Configurar minikube perquè doni external IPs als serveis de tipus LoadBalancer executant en una terminal 'minikube tunnel'. ALERTA!! No tancar aquesta terminal per deixar el tunnel obert.
7. Instal·lar el repositori de Kong: helm repo add kong https://charts.konghq.com && helm repo update
8. Desplegar Kong aplicant el helm chart de Kong i el values de la carpeta charts: helm upgrade --install kong kong/kong --values ./charts/values.yaml
9. Validar que el pod que executa l'eina de kong (kong-proxy-xxxxx) està executant-se correctament (running): kube -n kong get pods.  
10. Modificar l'/etc/hosts afegint una nova línia amb 'ip-container-minikube    admin.minikube.cat manager.minikube.cat
11. Comprovar que tenim accés al Kong Manager per mitjà del navegador amb http://manager.minikube.cat

## Configuració de l'API Gateway Kong via UI web
1. Obtenir la external-IP del servei kong-kong-proxy i modificar l'/etc/hosts afegint una nova línia amb 'external-ip   kong-api.minikube.cat' (el host que gestiona l'api gateway Kong)
2. Configurar les rutes, serveis necessaris per accedir als serveis /date i /store de l'aplicació rest-server. 
3. Comproveu que podeu accedir-hi (nota: els logs de kong es guarden al directori kong_prefix del container kong-proxy) 
    1. curl http://kong-api.minikube.cat/date  // {"date":"2024-12-04 09:32:15"}
    2. curl -X POST http://kong-api.minikube.cat/store -H "Content-Type: application/json" -d '{"a":1}'  // "message": "Data received and stored: {'a': 1}"
4. Crear un usuari (costumer) amb una credencial( p.e.  apikey: c182cca8a7c1cc3659369fdba0bc3f27a74c804fc8ebf738dd2ad9ba76a78c73).
5. Utilitzar plugins que permetin per customitzar el consum que pot fer aquest usuari dels serveis de l'aplicació rest-server (key-auth, rate-limit, ip-restric, request-max-size...)
