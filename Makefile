#!/bin/bash
#
# Purpose: File to configure before starting the vagrant

# DOCKER -------------------------------------------------------
file := "docker-compose.yml"

up:
	# Create the image and container, if the image is not present it will be builded
	sudo docker-compose -f ${file} up

build:
	# Create the image, container and force a build
	sudo docker-compose -f ${file} up --build

logs:
	# See the logs from all containers that are running
	sudo docker-compose -f ${file} logs -f -t

start:
	# Start containers
	sudo docker-compose -f ${file} start

stop:
	# Stop containers
	sudo docker-compose -f ${file} stop

ps:
	# Verify running containers
	sudo docker-compose -f ${file} ps

show-images:
	# Show installed images
	sudo docker images

down:
	# Shutdown containers and remove the images
	sudo docker-compose -f ${file} down

down-force:
	# Shutdown containers and and remove the volumes
	sudo docker-compose -f ${file} down -v

down-remove-images:
	# Shutdown containers, remove the images and remove the volumes.
	# The images will nedd to be rebuilded
	sudo docker-compose -f ${file} down --rmi local -v


# DJANGO -------------------------------------------------------
container := "web"

bash:
	# Get in the bash of container
	sudo docker exec -it ${container} /bin/sh

run:
	# Run a command inside docker
	sudo docker-compose -f ${file} run --rm ${container} ${command}

app: manage.py
	# Create a new app
	sudo docker-compose -f ${file} run --rm ${container} python manage.py startapp ${name}

createsuperuser: manage.py
	# Create a project super user
	sudo docker-compose -f ${file} run --rm ${container} python manage.py createsuperuser

shell: manage.py
	# Open an interactive shell to debug
	sudo docker-compose -f ${file} run --rm ${container} python manage.py shell

# DATABASE -----------------------------------------------------

migrations: manage.py
	# Create all migrations from models
	sudo docker-compose -f ${file} run --rm ${container} python manage.py makemigrations

migrations-merge: manage.py
	# Create migrations from models with the --merge flag
	sudo docker-compose -f ${file} run --rm ${container} python manage.py makemigrations --merge

migrate: manage.py
	# Migrate all migrations on database
	sudo docker-compose -f ${file} run --rm ${container} python manage.py migrate

sql: manage.py
	# Show SQL commands
	sudo docker-compose -f ${file} run --rm ${container} python manage.py sqlmigrate ${app_label} ${migration_name}

# TESTS --------------------------------------------------------
local := "**/test/"

test: manage.py
	# Run tests
	sudo docker-compose -f ${file} run --rm ${container} coverage run --source==${local} -m py.test 

test-all: manage.py
	# Run tests
	sudo docker-compose -f docker-compose.yml run --rm web  bash -c "coverage run --source . -m py.test && coverage report"

coverage-html: manage.py
	# Create a covarege page based on the tests
	sudo rm -rf htmlcov
	sudo docker-compose -f ${file} run --rm ${container} coverage html

# TRANSLATION --------------------------------------------------
files := "**/*.py"

messages:
	# Create a django.po to insert translations (pt-BR)
	sudo docker-compose -f ${file} run --rm ${container} django-admin makemessages -l pt_BR

compilemessages:
	# Create translations
	sudo docker-compose -f ${file} run --rm ${container} django-admin compilemessages

# STATIC FILES -------------------------------------------------

staticfiles: manage.py
	# Collect all static files
	sudo docker-compose -f ${file} run --rm ${container} python manage.py collectstatic

# DOCUMENTATION
doc: mkdocs.yml
	# Deploy all documentation
	mkdocs gh-deploy 

# HEROKU -------------------------------------------------

deploy-local: 
	# Deploy locally with heroku
	$(warning You need to be inside VENV or you will get some errors) 
	$(warning AND you need a procfile)  
	read -p "Press enter to continue"
	heroku local web
