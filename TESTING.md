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
| T013 | Register page route | Opened `/accounts/register/`. | Register page displays using the GameShelf auth layout. | Pass | Confirms custom register view and template are connected. |
| T014 | User registration | Submitted valid registration details. | User account is created and user is logged in. | Pass | Navbar updates to authenticated state after registration. |
| T015 | Login page route | Opened `/accounts/login/`. | Login page displays using the GameShelf auth layout. | Pass | Confirms Django login view uses the custom template. |
| T016 | User login | Logged out, then submitted valid login details. | User logs in successfully and authenticated navbar appears. | Pass | Confirms login redirect and session handling work. |
| T017 | User logout | Clicked `LOGOUT` in the navbar. | User logs out and navbar returns to logged-out state. | Pass | Logout uses a POST form with CSRF protection. |
| T018 | Register form validation | Submitted invalid or mismatched registration details. | Form reloads and displays a clear error message. | Pass | Confirms form validation errors are visible to the user. |
| T019 | Authenticated user register redirect | Visited `/accounts/register/` while logged in. | User is redirected to the homepage. | Pass | Prevents logged-in users from using the register page. |
| T020 | Game model setup | Added the `Game` model and ran `python manage.py check`. | Django reports no system check issues. | Pass | Confirms the main custom model matches the planned GameShelf collection fields. |
| T021 | Image upload dependency | Installed Pillow after adding the `ImageField`. | Pillow installs successfully and project check still passes. | Pass | Required for game image uploads. |
| T022 | Game migration creation | Ran `python manage.py makemigrations` after creating the `Game` model. | Django creates an initial migration for the games app. | Pass | Confirms Django can convert the model into a database table. |
| T023 | Game migration apply | Ran `python manage.py migrate`. | Game database table is created successfully. | Pass | Confirms the model is now available in the database. |
| T024 | Game admin setup | Registered the `Game` model in `games/admin.py`. | Django check passes with admin configuration. | Pass | Confirms the model can be managed through Django admin. |