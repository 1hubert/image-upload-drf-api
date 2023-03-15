# Image Upload Django Rest Framework API

## Overview

This API allows authenticated users to upload images and get their unique links.

I'm currently working on auto-generating thumbnails of various sizes based on the user account tier, as well allowing users with certain tiers to fetch an expiring link to a specified image.

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

## Run locally

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
