FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt

COPY luxembot.py links.txt credentials.json /app/

CMD ["python", "luxembot.py"]