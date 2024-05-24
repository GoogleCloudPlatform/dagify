# Stage 1: Build dagify Application
FROM python:alpine3.20
WORKDIR /app

COPY . .
RUN pip3 install -r ./requirements.txt

CMD ["python", "DAGify.py"]