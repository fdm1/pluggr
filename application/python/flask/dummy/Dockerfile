FROM python:3.7.4-stretch

WORKDIR /home/app
COPY requirements.txt /home/app
RUN pip install -r requirements.txt
COPY ./app/ /home/app

EXPOSE 5090
CMD ["python", "/home/app.py"]
