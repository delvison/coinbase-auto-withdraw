build:
	docker build -t coinbase-auto-transfer .

microk8s:
	docker save coinbase-auto-transfer > image.tar
	microk8s ctr image import image.tar
	rm image.tar
