#!/bin/sh

if [ "${1}" = "dev" ]; then
	exec fastapi dev api.py \
		--proxy-headers \
		--host 0.0.0.0 \
		--port 8000
else:
	exec fastapi run api.py \
		--proxy-headers \
		--host 0.0.0.0 \
		--bind 8000
fi
