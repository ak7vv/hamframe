#!/bin/sh
exec fastapi run api.py \
	--proxy-headers \
	--port 8000