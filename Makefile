build:
	docker build \
	-t coinbase-auto-withdraw:0.0.1 \
	-t localhost:32000/coinbase-auto-withdraw:0.0.1 \
	.

push:
	docker push localhost:32000/coinbase-auto-withdraw:0.0.1

microk8s:
	docker save coinbase-auto-withdraw:0.0.1 > image.tar
	microk8s ctr image import image.tar
	rm image.tar
