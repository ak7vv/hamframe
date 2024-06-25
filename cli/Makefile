all:
	cp ../requirements.txt .
	docker build --tag=hamframe-cli --compress=true --memory=2048 .

clean:
	-rm requirements.txt

dist-clean: clean
	-docker image rm hamframe-cli --force
	-docker image prune --force
	-docker builder prune --force