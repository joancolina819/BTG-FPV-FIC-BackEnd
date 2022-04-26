FROM python:3.9
# FROM ubuntu:16.04

# MAINTAINER  "Joan David Colina"


# RUN apt-get update -y && apt-get install -y python-pip python-dev sudo
# RUN sudo apt install -y curl
# RUN curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
# RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
# #RUN sudo apt update
# RUN sudo apt-get install -y mongodb-org-unstable
# RUN sudo systemctl start mongod.service
# RUN sudo systemctl enable mongod
# # 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./src /code/src

# 
CMD ["uvicorn", "src.gestion_fondos.gestor_fondos:app", "--host", "0.0.0.0", "--port", "80"]