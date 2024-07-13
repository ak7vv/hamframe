#!/bin/sh

if [ "${1}" = "dev" ]; then
	exec fastapi dev api.py
else:
	exec fastapi run api.py
fi
