FROM python:3.7

RUN pip install coinbase==2.1.0

ADD main.py .

CMD ["python", "main.py"]
