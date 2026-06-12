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
| T025 | Game form setup | Created `GameForm` and ran `python manage.py check`. | Django reports no system check issues. | Pass | Form includes editable game fields but does not expose the owner field. |
| T026 | Game title validation | Added validation requiring game titles to contain at least two characters. | One-character titles will be rejected by the form. | Pass | Validation will be manually tested when the add game page is created. |
| T027 | Game platform validation | Added validation requiring platform text to contain at least two characters. | One-character platform values will be rejected by the form. | Pass | Validation will be manually tested when the add game page is created. |
| T028 | Games route protection | Visited `/games/` while logged out. | User is redirected to the login page. | Pass | Confirms the games collection is protected by login. |
| T029 | Login redirect to games | Logged in with valid details. | User is redirected to the games collection page. | Pass | `LOGIN_REDIRECT_URL` points to `games_list` after the route was created. |
| T030 | Games page layout | Opened `/games/` while logged in. | Games page displays sidebar filters and table panel. | Pass | Layout follows the planned wireframe. |
| T031 | Empty games state | Opened games page with no games saved. | Empty state message displays. | Pass | Confirms the template handles an empty collection. |
| T032 | Games navbar link | Clicked `GAMES` in the authenticated navbar. | Browser opens `/games/`. | Pass | Confirms navbar route is connected. |
| T033 | Table heading sort links | Clicked table heading sort links on the empty games table page. | Page reloads without error. | Pass | Sorting links are available and safe even before games are added. |
| T033 | Table heading sort links | Clicked table heading sort links on the empty games table page. | Page reloads without error. | Pass | Sorting links are available and safe even before games are added. |
| T034 | Add game route | Clicked `ADD GAME` from the games page. | Add Game form opens. | Pass | Confirms the create route, view and template are connected. |
| T035 | Add game form display | Opened the Add Game page. | Game fields, favourite checkbox and image upload field are visible. | Pass | Initial field rendering issue was fixed by replacing `as_field_group` with explicit label, field and error rendering. |
| T036 | Create game | Submitted valid game details. | Game is saved and user is redirected to the games list. | Pass | New game appears in the table. |
| T037 | Game owner assignment | Created a game while logged in. | Game belongs to the logged-in user automatically. | Pass | Owner field is not exposed in the form and is set in the view. |
| T038 | Game image upload field | Opened the Add Game form. | Image upload field is displayed. | Pass | Field is visible; actual upload/save will be tested when media display is added. |
| T039 | Favourite field | Tick marked a game as favourite during creation. | Game saves with favourite status. | Pass | Favourite value appears in the games table. |
| T040 | Game form validation | Submitted one-character title and platform values. | Form rejects invalid data and displays errors. | Pass | Confirms custom `GameForm` validation works. |
| T041 | Edit game route | Clicked `Edit` on a saved game. | Edit Game form opens with existing game details filled in. | Pass | Confirms update route, view and form instance are connected. |
| T042 | Update game | Changed a saved game's details and submitted the form. | Game updates and user is redirected to the games list. | Pass | Success message confirms update. |
| T043 | Delete game route | Clicked `Delete` on a saved game. | Delete confirmation page opens. | Pass | Confirms delete route and template are connected. |
| T044 | Cancel delete | Clicked `Cancel` on the delete confirmation page. | User returns to the games list and the game remains saved. | Pass | Confirms users can safely back out of deletion. |
| T045 | Confirm delete | Confirmed deletion of a saved game. | Game is deleted and user is redirected to the games list. | Pass | Success message confirms deletion. |
| T046 | Game ownership protection | Edit/delete views use `get_object_or_404(Game, pk=pk, owner=request.user)`. | Users can only access their own game records. | Pass | Protects user-owned data from being edited or deleted by another user. |
| T047 | Media URL setup | Added media serving to `config/urls.py` and ran `python manage.py check`. | Django reports no system check issues. | Pass | Uploaded files can be served during local development. |
| T048 | Create game with image | Added a game with an uploaded image. | Game saves and image thumbnail appears in the games table. | Pass | Confirms image upload and display work locally. |
| T049 | Edit game image preview | Opened the edit form for a game with an uploaded image. | Current image appears in the image preview area. | Pass | Confirms uploaded image is available on edit. |
| T050 | Game without image | Added or viewed a game with no image uploaded. | Table displays `No image` instead of a broken image. | Pass | Confirms empty image field is handled safely. |
| T051 | Profile route protection | Visited `/accounts/profile/` while logged out. | User is redirected to the login page. | Pass | Confirms profile is protected by login. |
| T052 | Profile navbar link | Clicked `PROFILE` while logged in. | Profile page opens. | Pass | Confirms navbar route is connected. |
| T053 | Profile user details | Viewed profile page while logged in. | Username and email/account information display correctly. | Pass | Email displays fallback text when no email is saved. |
| T054 | Profile account tier | Viewed profile page while logged in. | Account tier displays as Free. | Pass | Premium tier will be added later through Stripe. |
| T055 | Profile statistics | Viewed profile after creating games. | Total games, favourites and platform count display correctly. | Pass | Confirms stats are calculated from the logged-in user's games. |
| T056 | Game type statistics | Viewed profile after adding games. | Collection by type counts display correctly. | Pass | Confirms the profile loops through `Game.GAME_TYPE_CHOICES`. |
| T057 | Custom logout view | Clicked `LOGOUT` while logged in. | User is logged out and redirected to the homepage. | Pass | Logout now uses a custom view in `accounts.views`. |
| T058 | Logout success message | Logged out through the navbar form. | Success message appears on the homepage. | Pass | Confirms user feedback is shown after logout. |
| T059 | Logout POST protection | Confirmed logout is submitted through a POST form with CSRF token. | Logout is protected from simple GET link actions. | Pass | Improves authentication safety. |
| T060 | Change password route | Clicked `Change Password` from the profile page. | Password change page opens. | Pass | Uses Django's built-in auth URL routes. |
| T061 | Styled password change page | Clicked `Change Password` from the profile page. | Styled GameShelf password change form displays. | Pass | Overrides Django's default `password_change_form.html` template. |
| T062 | Password change validation | Submitted the password change form with empty or invalid fields. | Form reloads and displays validation errors. | Pass | Confirms Django validation is visible in the styled template. |
| T063 | Successful password change | Submitted valid old password and matching new password values. | Password is changed and success page displays. | Pass | Confirms Django's password change flow works. |
| T064 | Styled password success page | Viewed password change done page after successful update. | Styled GameShelf success page displays. | Pass | Overrides Django's default `password_change_done.html` template. |
| T065 | Login with new password | Logged out and logged back in using the new password. | Login succeeds with the updated password. | Pass | Confirms the password was actually changed. |
| T066 | Profile tab navigation | Viewed profile and password change pages. | Profile/Change Password buttons display on both pages with the active page highlighted. | Pass | Improves navigation clarity between account pages. |