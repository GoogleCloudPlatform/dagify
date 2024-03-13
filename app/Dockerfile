# Stage 1: Build Web Application
FROM node:current-alpine3.19 as build-stage 
WORKDIR /web
COPY /web/package*.json ./
RUN npm install
COPY ./web .
RUN npm run build


# Build API Application
FROM python:3.11.7

WORKDIR /app
COPY --from=build-stage /web/dist/dist /app/dist/
COPY --from=build-stage /web/dist/index.html /app/dist/index.html

COPY ./app .
RUN pip3 install -r /app/requirements.txt

ARG BUILD_PORT=8080
ENV PORT=$BUILD_PORT

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]