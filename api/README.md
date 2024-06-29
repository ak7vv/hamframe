# API

## Overview

The API is implemented as a Docker container running gunicorn/uvicorn/FastAPI.  The container can be built with _make_ within the API directory.

You can run the container in FastAPI's dev or prod mode depending on whether you pass _'dev'_ as an argument to the _docker run_ command:

docker run --rm --name hamframe-api --publish 8000:8000 hamframe-api
docker run --rm --name hamframe-api --publish 8000:8000 hamframe-api dev

The API is then exposed on 8000/tcp and bound to 0.0.0.0 (you can access it from outside of the host).

FastAPI is self-documenting as OpenAPI, which can be found at

http://host_ip:8000/openapi.json

You can also find human-readable variants here:

    http://host_ip:8000/docs
    http://host_ip:8000/redoc

where you can learn about the API verbs and attributes as well as exercise the API.

## FastAPI dev mode

If you've launched the API container as described above, you can iterate through code versions by executing this command:

docker cp api.py hamframe-api:/hamframe

FastAPI will detect the change and relaunch with the new version.  You still need to rebuild the container image as described above if you want this change to persist.
