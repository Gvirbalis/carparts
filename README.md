1.About:
    
This is a website for used car parts. I am still updating it. On the website, you can add cars and parts.
Parts can be linked to a car, so if you choose a part type, such as "Engine," the part description will show the engine code.
Don't forget, if you want to give some users permission to add cars or parts, you need to go to the admin panel, 
click on "Profiles," select the user, change their status to "Verified," and save it!

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

3. In Admin side you need add:

   Car Models.
   Part types.

6. Contacts:


github: https://github.com/Gvirbalis

Email: gvirbalis994@gmail.com

