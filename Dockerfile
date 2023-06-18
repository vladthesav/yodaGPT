FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 3500

#set this env variable so programs know it's running in a container
ENV container=True 

CMD ["python3","app.py"]