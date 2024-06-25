all:
	cp ../requirements.txt .
	docker build --tag=hamframe-cli --compress=true --memory=2048 .

clean:
	-rm requirements.txt

dist-clean: clean
	-docker builder prune --force
	-docker image rm hamframe-cli --force
	# this shouldn't be needed but things happen
	-docker image prune --force
