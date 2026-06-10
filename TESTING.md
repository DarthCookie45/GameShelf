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
| T008 | Home page route | Opened `/` after adding the home view, URL and template. | GameShelf homepage loads successfully. | Pass | Confirms the pages app is connected to the project URLs. |
| T009 | Homepage app explanation | Viewed the homepage content. | Homepage explains what GameShelf does and why users would create an account. | Pass | About-style information is included on the homepage instead of using a separate About page. |
| T010 | Shared layout on homepage | Viewed the homepage. | Page uses the shared navbar and GameShelf theme. | Pass | Confirms the template extends `base.html`. |
| T011 | Homepage feature panels | Viewed the homepage. | Three feature panels are visible. | Pass | Confirms homepage content is displayed as planned. |
| T012 | Logged-out navbar links | Viewed the homepage while logged out. | Navbar only shows Home and Login/Register links. | Pass | App-only links are hidden until the user is authenticated. |