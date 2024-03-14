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
COPY --from=build-stage /web/dist/dist /app/app/web/dist
COPY --from=build-stage /web/dist/index.html /app/app/web/dist/index.html

COPY /converters .
COPY /app .
RUN pip3 install -r ./requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "wsgi:create_app()"]