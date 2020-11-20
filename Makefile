.PHONY: run
run: app.py
	FLASK_APP=app.py FLASK_ENV=development flask run --host=0.0.0.0

.PHONY: init_db
init_db:
	python manage.py db init

.PHONY: remove_db
	python manage.py db remove
