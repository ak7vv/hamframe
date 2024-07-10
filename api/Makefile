
## NOT MAINTAINED: Using GitHub Actions instead. See ../.github/workflows

all: hamframe-api

hamframe-api:
	docker build \
		--tag=hamframe-api \
		--compress=true \
		--memory=2048 \
		.
	docker image ls hamframe-api

clean:
	-docker image prune --force
	-docker builder prune --force
	# clean up when --rm is not specified
	-docker rm `docker ps -a -f status=exited | awk '{ print $$1 }' | grep -v CONTAINER`

dist-clean: clean
	-docker image rm hamframe-api --force

