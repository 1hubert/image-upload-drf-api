# Image Upload Django Rest Framework API

## Overview

This API allows authenticated users to upload images and get their unique links.

## Running the Django app

### Run with Docker

1) Build a docker container
```
$ docker compose build
```
2) Start all the services defined in `docker-compose.yml`. You should be able to access the Django app at [127.0.0.1:8000/](http://127.0.0.1:8000/)
```
$ docker compose up
```
3) Stop running containers & clean up:
```
$ docker compose down
```

### Run locally

1) Install dependencies using the Python Package Manager
```
$ pip install -r requirements.txt
```
2) Change directory to the Django project folder
```
$ cd imageupload
```
3) Apply migrations to the database
```
$ python manage.py migrate
```
3) Run the server with `manage.py`. You should be able to access the Django app at [127.0.0.1:8000/](http://127.0.0.1:8000/)
```
$ python manage.py runserver
```

## Endpoints

|       Intent       |   Endpoint  | HTTP Request |                    Payload                   |              Response              |
|:------------------:|:-----------:|:------------:|:--------------------------------------------:|:----------------------------------:|
|     List images    | /api/images |      GET     |                       -                      | [{"id": 0, "image_url": "string"}] |
| Upload a new image | /api/images |     POST     |                image (binary)                |  {"id": 0, "image_url": "string"}  |
|       Log In       | /user/login |     POST     | {"username": "string", "password": "string"} |                  -                 |
