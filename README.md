1.About:
    
    This is a used car parts website.
    I am still updating

2.How to make it work:

First u need check requirements.txt for make sure all library's installed :
    
    $ pip install -r requirements.txt

Second create database at Terminal:
    
    $python manage.py makemigrations
    $python manage.py migrate

Create Admin account at Terminal:
    
    $python manage.py createsuperuser

At mysite/settings.py you need configurate:

EMAIL_USE_TLS = True

EMAIL_HOST = {'your mail host'}

EMAIL_PORT = {'email port'}

EMAIL_HOST_USER = {'email'}

EMAIL_HOST_PASSWORD = {'password'}

DEFAULT_FROM_EMAIL = {'email'}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SERVER_EMAIL = {'server mail'}


Final launch:

    $python manage.py runserver

3. In Admin side you need add Car Models.

4. Contacts:


github: https://github.com/Gvirbalis

Email: gvirbalis994@gmail.com

