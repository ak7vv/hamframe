all: prep cli

prep:
	if [ -n ${VIRTUAL_ENV} ]; then . .venv/bin/activate; fi
	pip freeze > requirements.txt

cli: prep
	( cd cli; make )

clean:
	( cd cli; make clean )

dist-clean: clean
	( cd cli; make dist-clean )

