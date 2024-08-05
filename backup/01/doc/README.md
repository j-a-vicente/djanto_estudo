# SentinelDataS_Web

Projeto

Order de execução do projeto.


Comando executados no shell
````
python -m pip install --upgrade pip
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip

pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage

pip install mysqlclient

pip freeze > requirements.txt

# criar o projeto.
django-admin startproject SentinelWeb .

# criar a aplicação.
django-admin startapp core



# agora criando as tabelas no banco de dados.
python .\manage.py migrate 

python .\manage.py makemigrations

# Iniciar o projeto.
python .\manage.py runserver

````


antes de criar o usuário administrador tem que criar a estrutura do banco.
````
python .\manage.py migrate 

# criar o usuário de administração da console do django
python .\manage.py createsuperuser
````
