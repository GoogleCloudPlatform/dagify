FROM python:alpine3.20

WORKDIR /app

COPY . .

RUN pip3 install -r ./requirements.txt

EXPOSE 8000

ADD entrypoint.sh /usr/src/app/entrypoint.sh

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]