IMAGE_NAME=rest-server
SERVICE_PORT=2000

build:
	docker build -t ${IMAGE_NAME} .

run:
	docker run --network=host -p $(SERVICE_PORT):$(SERVICE_PORT) --name=${IMAGE_NAME} ${IMAGE_NAME}

