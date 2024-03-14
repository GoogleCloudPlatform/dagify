# Stage 1: Build Web Application
FROM node:current-alpine as build-stage 
WORKDIR /web
COPY /web/package*.json ./
RUN npm install
COPY ./web .
RUN npm run build


# Build API Application
FROM python:alpine

WORKDIR /app
COPY --from=build-stage /web/dist/dist /app/dist/
COPY --from=build-stage /web/dist/index.html /app/dist/index.html

COPY /converters .
COPY /app .
RUN pip3 install -r ./requirements.txt

ARG BUILD_PORT=8080
ENV PORT=$BUILD_PORT

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app"]