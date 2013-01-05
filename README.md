SAE Django
=========

Basic codes for django 1.4 on SAE.


Usage
=========
If you want to use this code base, please£º
1. Change the app name in config.yaml first.
2. Change SECRET_KEY in rootapp/settings.py


How this is created
=========
The following step is used to create the project:

1. Checkout basic SAE python website in a single version (SAE gave 1-9 version of app)
2. Start a project using: python django-admin.py startproject rootapp (I used rootapp for this project, can be anything else
3. Copy manage.py and rootapp folder to SAE folder for a version.
4. Edit index.wsgi as in this repo.
5. Access SAE web site, "Congratulations on your first Django-powered page." should be displayed.


Ref
=========

http://blog.chedushi.com/archives/3598
http://www.cnblogs.com/qtsharp/archive/2012/01/12/2320774.html