all: prep cli api

prep:
	if [ -n ${VIRTUAL_ENV} ]; then . .venv/bin/activate; fi
	pip freeze > requirements.txt

cli: prep
	( cd cli; make )

cli-clean:
	( cd cli; make clean )

cli-dist-clean: clean
	( cd cli; make dist-clean )

api: prep
	( cd api; make )

cli-clean:
	( cd api; make clean )

api-dist-clean: clean
	( cd api; make dist-clean )

clean: cli-clean api-clean

dist-clean: cli-dist-clean api-distclean

