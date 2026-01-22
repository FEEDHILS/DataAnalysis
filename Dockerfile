FROM python:latest

WORKDIR /usr/src/TaxiData
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY generator.py .
COPY main.py .

CMD [ "python", "main.py" ]