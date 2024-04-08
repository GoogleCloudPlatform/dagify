# Stage 1: Build AirShip Application
FROM python
WORKDIR /app

COPY . .
RUN pip3 install -r ./requirements.txt

CMD ["python", "AirShip.py"]
