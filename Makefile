run: env feedback.db
	./env/bin/python manage.py run

env:
	virtualenv env
	pip install --upgrade -s -E env -r requirements.txt

feedback.db: env
	./env/bin/python manage.py initdb

clean:
	find . -name "*.pyc" | xargs rm -f

superclean:
	rm -rf env feedback.db

push:
	rsync -e ssh -avz * root@styx.nuxeo.com:/var/www/nuxeo-feedback/

