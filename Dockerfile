# Stage 1: Build Web Application
FROM node:current-alpine as build-stage 
WORKDIR /web
COPY /web/package*.json ./
RUN npm install
COPY ./web .
RUN npm run build


# Build API Application
FROM python
WORKDIR /app

COPY /converters .
COPY /app .
RUN pip3 install -r ./requirements.txt

COPY --from=build-stage /web/dist/static /app/app/static
COPY --from=build-stage /web/dist/index.html /app/app/templates/index.html

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "8", "--log-level", "DEBUG", "wsgi:create_app()"]