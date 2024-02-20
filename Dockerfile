FROM python3.9

RUN apt update && apt upgrade -y
RUN apt-get -y update
RUN apt install git curl python3 python3-pip -y
RUN pip3 install -U pip
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
CMD python3 KanishkaSpam.py
