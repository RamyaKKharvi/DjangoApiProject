DjangoApiProject
This repo will include Api projects built with django and DRF
Project to demonstrate django CRUD operations.

Started django project named "ClubManagement" and created an app named "Membership" inside the project.  
App name was written in settings.py file inside INSTALLED_APPS. 
Created a "Member" class model in models.py file and also created class "SubscriberChoices" which was inherited inside attribute "subscriber_type".
Created forms.py file and created "MemberForm" form inside it.
Templates were created to update, delete and delete data.
Member Create, Retrieve, Update and Delete class were created by using methods from inheriting View, TemplateView, and RedirectView class inside views.py file.
Created config.py file and year calculation was assigned to variable "MEMBERSHIP_DURATION".
Created service.py file and inside it defined two functions to get subscription renewal date from_subscriber type and subscription_date and to get membership end date from membership start date.
Defined urls inside settings.py and urls.py file. Created a script that will hit the given API endpoint & create, read, update, delete, and store the data received from the response to a database table.