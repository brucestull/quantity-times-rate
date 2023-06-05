# Useful Commands and Links

## Commands

### This Project

1. `pipenv install`
1. `pipenv shell`
1. `python manage.py migrate`
1. `python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`

### Django Create `SECRET_KEY`

* `python manage.py shell`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`

### Heroku

* `heroku run python manage.py createsuperuser --email admin@email.app --username admin`
* `heroku run python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`
* `heroku login`

## Development Server Links

* Server Root:
  * <http://localhost:8000/>
* Boosts:
  * <http://localhost:8000/boosts/>
  * <http://localhost:8000/boosts/inspirationals/>
* API:
  * <http://localhost:8000/api/v1/>

## Production deployment links

* Server Root:

## Repository Links

* Repository [`README.md`](../README.md)
