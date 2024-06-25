all:
	cp ../requirements.txt .
	docker build --tag=hamframe-cli --compress=true --memory=2048 .

clean:
	-rm requirements.txt
	-docker image rm hamframe-cli --force

dist-clean: clean
	-docker builder prune --force
