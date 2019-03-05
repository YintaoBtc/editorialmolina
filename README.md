## Proyecto para la editorial La Tirla la Tierra

Desarollo en django con docker. 

Paginas:

1. Portada
1. Historia
1. Libros
1. Autores
1. Visitanos
1. Contacto

Panel Administrador
1. Gestion de usuarios
1. Gestion de libros
1. Gestion de autores
1. Gestion de redes sociales
1. Gestion de paginas secundarias

## Django Development With Docker Compose and Machine

Featuring:

- Docker v1.10.3
- Docker Compose v1.6.2
- Docker Machine v0.6.0
- Python 3.5

Blog post -> https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/

### OS X Instructions

1. Start new machine - `docker-machine create -d virtualbox dev;`
1. Configure your shell to use the new machine environment - `eval $(docker-machine env dev)`
1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. Create migrations - `docker-compose run web /usr/local/bin/python manage.py migrate`
1. Grab IP - `docker-machine ip dev` - and view in your browser
