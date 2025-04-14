all: prep cli api

prep:
	# assume we're on something Debian'ish with apt
	sudo apt-get install --yes \
		git \
		python3-dev \
		python3-pip \
		python3-setuptools \
		build-essential \
	       	libssl-dev
	if [ -n ${VIRTUAL_ENV} ]; then . .venv/bin/activate; fi
	pip freeze > requirements.txt

cli: prep
	( cd cli; make )

cli-clean:
	( cd cli; make clean )

cli-dist-clean: cli-clean
	( cd cli; make dist-clean )

api: prep
	( cd api; make )

api-clean:
	( cd api; make clean )

api-dist-clean: api-clean
	( cd api; make dist-clean )

clean: cli-clean api-clean

dist-clean: cli-dist-clean api-distclean

