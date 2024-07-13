# API

# **OUT OF DATE**

## TOC

[Architecture](#architecture)
- [Configuration](#configuration)
<P>

[Background](#background)

[FastAPI dev mode](#fastapi-dev-mode)

### Configuration 

Configuration is stored in a [Redis](redis.io)-compatible key-value store ([KVS](https://en.wikipedia.org/wiki/Key%E2%80%93value_database)).  The API is a lightweight abstraction to store (_import_), retrieve (_export_), and _delete_ JSON encoded configuration objects within KVS. Multiple sets of configurations can be managed by naming different _instances_.  Within an instance, multiple _sections_ can be defined.  This results in keys being encoded in KVS as _config:\<instance\>:\<section\>_, like _config_:_ak7vv_:_n0nbh_ for a configuration section _n0nbh_ within the instance _ak7vv_.

The value associated with a key is encoded as a JSON object and not validated beyond being valid JSON.  Lightweight abstraction means the responsibility for validating and understanding encoded JSON data rests with the consumers of the API for the value part of anything stored in KVS.

One example of a consumer of the API are the CLI commands in [../cli](../cli) that invoke REST API calls to implement the CLI backend.  Components integrated with Hamframe can use the API to retrieve or modify configuration sections.

If _section_ is not specified in the API call, the operation will assume _section_ to be a wildcard and potentially match multiple _sections_ within the same _instance_ if they exist. Each section is returned as a numbered enumeration of the resulting array.  The response message in the body of the request indicates number of sections were matched with the property _"sections:"_ with an integer value.

## Background

The API is implemented as a Docker container running gunicorn/uvicorn/[FastAPI](https://fastapi.tiangolo.com/).  The container can be built with _make_ within the API directory.

You can run the container in FastAPI's _dev_ or _prod_ mode depending on whether you pass _'dev'_ as an argument to the _docker run_ command:

    docker run --rm --name hamframe-api --publish 8000:8000 hamframe-api

or

    docker run --rm --name hamframe-api --publish 8000:8000 hamframe-api dev

The API is then exposed on _8000/tcp_ and bound to _0.0.0.0_ (this means you can access it from outside of the host).

FastAPI is self-documenting as [OpenAPI](https://www.openapis.org/) (the artist formerly known as Swagger), which can be found at

    http://host_ip:8000/openapi.json

You can also find human-readable variants here:

    http://host_ip:8000/docs
    http://host_ip:8000/redoc

where you can learn about the API verbs and attributes as well as exercise the API.

## FastAPI dev mode

If you've launched the API container as described above, you can iterate through code versions by executing this command:

    docker cp api.py hamframe-api:/hamframe

FastAPI will detect the change and relaunch with the new version.  You still need to rebuild the container image as described above if you want this change to persist.

