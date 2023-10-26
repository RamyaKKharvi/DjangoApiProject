## Project to demonstrate django CRUD operations.

### Requirements:
* Python 3.10.12
* Django 4.2.3

### Steps to run this project:
1. Create virtual environment using `python -m venv 'ClubManagementenv'` command.
2. Activate virtual environment using `source ClubManagementenv/bin/activate` command.
3. Install requirements using `pip install -r requirements.txt` command.
4. Start new project using `django-admin startproject ClubManagement` command.
5. Change directory to django project `cd ClubManagement`
6. Start django application using command `python manage.py startapp Membership`
7. Add app name to setting.py file of django project in INSTALLED_APP
8. Create model class in models.py file django project.
9. Run `python manage.py makemigrations` command to convert class to query and `python manage.py migrate` command to create database table.
10. Create form class in forms.py file.
11. Create required templates
12. Write view function in view.py file 
13. Write urlpatterns in urls.py file of django project. 
14. Include applications url.py file inside Project url.py file. 
15. Run server `python manage.py runserver`
