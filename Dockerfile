FROM python:3.7

RUN pip install coinbase==2.1.0 &&\
  pip install git+https://github.com/mcdallas/cryptotools.git@master#egg=cryptotools

ADD main.py .

CMD ["python", "main.py"]
