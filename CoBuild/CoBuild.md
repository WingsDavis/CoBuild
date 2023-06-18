<!-- Getting started with CoBuild -->
This project assumes you know how basics of create Django and React
This project was Biult with Django and React

Dependencies
python
npm

### Create a Development Environment
In the project Directory, you can run

### `django-admin startproject projectname .`
demo/
	__init__.py
	settings.py
	urls.py
	asgi.py
	wsgi.py
manage.py
### `python manage.py startapp appname`
app/
	__init__.py
	admin.py
	apps.py
	migrations

Run the app in the development mode.
### `python manage.py runserver`

The page will reload when you make changes

<!-- Creating a React Folder -->
React folder name as design

<!-- Link React to Django -->

In `settings.py` in demo
### type 'import os'  in line 1

Under Templates in 'DIRS' 
### type 'os.path.join(BASE_DIR, 'design/build')'

under the 'settings code'
### type 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'design/build/static') 
]'

In `urls.py` in demo
### add `from django.views.generic import TemplateView`
### in urlspatterns add 'path('', TemplateView.as_view(template_name = 'index.html'))'