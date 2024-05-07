# Stage 1: Build dagify Application
FROM python
WORKDIR /app

COPY . .
RUN pip3 install -r ./requirements.txt

CMD ["python", "DAGify.py"]