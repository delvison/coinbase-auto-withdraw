build:
	docker build -t coinbase-auto-transfer:0.0.1 .

microk8s:
	docker save coinbase-auto-transfer:0.0.1 > image.tar
	microk8s ctr image import image.tar
	rm image.tar
