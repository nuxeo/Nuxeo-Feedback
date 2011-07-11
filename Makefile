run: env feedback.db
	./env/bin/python manage.py run

env: requirements.txt
	virtualenv env
	pip install --upgrade -s -E env -r requirements.txt

feedback.db: env
	./env/bin/python manage.py initdb

clean:
	find . -name "*.pyc" | xargs rm -f
	rm -rf tmp

superclean:
	rm -rf env feedback.db

push:
	fab deploy

