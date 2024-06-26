all: hamframe-cli

hamframe-cli:
	cp ../requirements.txt .
	docker build \
		--tag=hamframe-cli \
		--compress=true \
		--memory=2048 \
		.
	docker image ls hamframe-cli

clean:
	-rm requirements.txt

dist-clean: clean
	-docker image rm hamframe-cli --force
	-docker image prune --force
	-docker builder prune --force
	-docker rm `docker ps -a -f status=exited | awk '{ print $$1 }' | grep -v CONTAINER`

