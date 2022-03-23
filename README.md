# Coinbase Auto Withdraw

Python script that can make Bitcoin auto-withdrawals from Coinbase.

Use Case:

I want to withdraw to my cold storage wallet any time I have a Bitcoin balance
over a certain amount.

# Deploy to microk8s

1. build docker image
```
make build
```
2. import image to microk8s
```
make microk8s
```
3. insert base64 encoded secrets into `k8s/secret.yml` file
4. deploy to microk8s
```
microk8s.kubectl apply -f k8s/secret.yml
microk8s.kubectl apply -f k8s/cronjob.yml
```
