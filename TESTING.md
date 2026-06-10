# Testing

This file records manual testing completed throughout development.

| Test ID | Feature | Action | Expected Result | Result | Notes |
| --- | --- | --- | --- | --- | --- |
| T001 | Django project setup | Ran `python manage.py runserver` after creating the Django project and apps. | Development server starts successfully. | Pass | Confirmed the project was created correctly. |
| T002 | Django welcome page | Opened `http://127.0.0.1:8000/` in the browser. | Django welcome page is displayed. | Pass | Confirms the base project works before custom code is added. |
| T003 | Initial database migrations | Ran `python manage.py migrate`. | Built-in Django migrations apply successfully. | Pass | Created database tables for admin, auth, contenttypes and sessions. |
| T004 | App registration | Added `pages`, `accounts`, `games` and `checkout` to `INSTALLED_APPS`, then ran `python manage.py check`. | Django reports no system check issues. | Pass | Confirms Django recognises the project apps. |
| T005 | Template directory setup | Added `BASE_DIR / 'templates'` to template `DIRS`. | Global templates folder is available for shared layouts. | Pass | `base.html` will be used by future pages. |
| T006 | Static/media settings | Added static and media settings in `settings.py`. | Project is prepared for custom CSS/JS and uploaded game images. | Pass | Media upload functionality will be used later for game images. |
| T007 | Theme shell CSS | Created `base.html` and `static/css/style.css`. | Shared layout and GameShelf theme files are present. | Pass | Visual shell follows the wireframe direction: dark navbar and matcha accent. |