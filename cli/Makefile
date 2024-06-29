all: hamframe-cli

hamframe-cli:
	docker build \
		--tag=hamframe-cli \
		--compress=true \
		--memory=2048 \
		.
	docker image ls hamframe-cli

clean:
	-docker image prune --force
	-docker builder prune --force
	# clean up when --rm is not specified
	-docker rm `docker ps -a -f status=exited | awk '{ print $$1 }' | grep -v CONTAINER`

dist-clean: clean
	-docker image rm hamframe-cli --force

