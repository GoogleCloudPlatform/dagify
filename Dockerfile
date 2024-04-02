# Stage 1: Build AirShip Application
FROM python
WORKDIR /app

COPY . .
RUN pip3 install -r ./requirements.txt

CMD ["sh", "-c", "Python3", "AirShip.py", "--source-path", "${SOURCE_PATH}", "--output-path", "${OUTPUT_PATH}",  "--temples-path", "${TEMPLATES_PATH}", "--config-file", "${CONFIG_FILE}"]