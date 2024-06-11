# Alcances
- API usando django
    - login
    - register
    - people
        - paginado
        - filtros
            - nombre
            - color de cabello
            - genero
    - inicio de pruebas unitarias
- Vistas principales (No funcionales)
    - Login
    - Home

# Ejecutar API Local
## Requisitos:
    python3.X
## Comandos
```bash
cd api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data #carga de los datos desde SWAPI
source .env
python manage.py runserver
```
### * Si se quiere user el admin de Django
```bash
python manage.py createsuperuser
```
### * Se cuenta con la colección de postman
### URL Prod
- *
# Ejecutar Web Client
## Requisitos:
    node18.16.x
## Comandos
```bash
cd web-client
npm i
npm run dev
```

### URL Prod
- https://main.d36s1uq99pfjuv.amplifyapp.com
