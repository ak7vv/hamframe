all: hamframe-api

hamframe-api:
	cp ../requirements.txt .
	docker build \
		--tag=hamframe-api \
		--compress=true \
		--memory=2048 \
		.
	docker image ls hamframe-api

clean:
	-rm requirements.txt
	-docker image prune --force
	-docker builder prune --force
	# clean up when --rm is not specified
	-docker rm `docker ps -a -f status=exited | awk '{ print $$1 }' | grep -v CONTAINER`

dist-clean: clean
	-docker image rm hamframe-api --force

