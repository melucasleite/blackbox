PROJECT_NAME = blackbox


.EXPORT_ALL_VARIABLES:

FLASK_DEBUG = True

venv: venv/bin/activate

venv/bin/activate: server/requirements.txt
	cd server && test -d venv || virtualenv venv
	cd server && venv/bin/pip install -Ur requirements.txt
	cd server && touch venv/bin/activate

venv-clean:
	cd server && rm -rf venv

npm-clean:
	cd client && rm -rf node_modules

npm-init:
	cd client && npm i

db-init: db-stop db-clean db-start

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
	cd server && export FLASK_DEBUG=True
	cd server && venv/bin/flask db upgrade
	cd server && venv/bin/python app.py

clean: db-clean venv-clean npm-clean

init: clean db-start venv npm-init

server-start-mock:
	make server-start MOCK_INTERFACE=True

client-start:
	cd client && npm start