PROJECT_NAME = blackbox


.EXPORT_ALL_VARIABLES:

FLASK_DEBUG = True

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate

venv-clean:
	rm -rf venv

db-start:
	docker-compose -p $(PROJECT_NAME) -f 'scripts/db.yml' up -d

db-stop:
	docker stop $$(docker ps -a -q)

db-clean:
	@docker-compose -p $(PROJECT_NAME) -f 'scripts/db.yml' down --remove-orphans --rmi all 2>/dev/null \
	&& echo 'Image(s) for "$(PROJECT_NAME)" removed.' \
	|| echo 'Image(s) for "$(PROJECT_NAME)" already removed.'

db-logs:
	docker-compose -p $(PROJECT_NAME) -f 'scripts/db.yml' logs -f

server-start: venv
	export FLASK_DEBUG=True
	venv/bin/flask db upgrade
	venv/bin/python run.py

clean: db-clean venv-clean

init: clean db-start venv

start: server-start
