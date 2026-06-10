# Testing

This file records manual testing completed throughout development.

| Test ID | Feature | Action | Expected Result | Result | Notes |
| --- | --- | --- | --- | --- | --- |
| T001 | Django project setup | Ran `python manage.py runserver` after creating the Django project and apps. | Development server starts successfully. | Pass | Confirmed the project was created correctly. |
| T002 | Django welcome page | Opened `http://127.0.0.1:8000/` in the browser. | Django welcome page is displayed. | Pass | Confirms the base project works before custom code is added. |
| T003 | Initial database migrations | Ran `python manage.py migrate`. | Built-in Django migrations apply successfully. | Pass | Created database tables for admin, auth, contenttypes and sessions. |