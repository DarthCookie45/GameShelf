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
| T067 | PlaySession model setup | Added `PlaySession` model and ran `python manage.py check`. | Django reports no system check issues. | Pass | Confirms second custom model and relationship to `Game` are valid. |
| T068 | PlaySession migration | Ran `python manage.py makemigrations` and `python manage.py migrate`. | PlaySession database table is created successfully. | Pass | Confirms the model was added to the database. |
| T069 | PlaySession admin setup | Registered `PlaySession` in Django admin and ran checks. | Django reports no admin configuration issues. | Pass | Confirms play sessions can be managed through admin if needed. |
| T070 | PlaySession form setup | Added `PlaySessionForm` and ran checks. | Django reports no form-related issues. | Pass | Form will be used when adding play session pages. |
| T071 | Profile play session statistic | Viewed profile after adding PlaySession count to context. | Profile displays play session count. | Pass | Confirms profile stats can include related model data. |
| T072 | Log play session route | Clicked `Log Play` for a saved game. | Play session form opens for the selected game. | Pass | Confirms play session route and ownership lookup work. |
| T073 | Create play session | Submitted valid play session details. | Play session is saved and user is redirected to the games list. | Pass | Success message confirms the session was added. |
| T074 | Play session game relationship | Created a play session from a game row. | Play session is attached to the selected game. | Pass | The game field is set in the view and not exposed to the user. |
| T075 | Play session validation | Submitted the play session form with missing/invalid player details. | Form displays validation errors. | Pass | Confirms `PlaySessionForm` validation works. |
| T076 | Profile play session count update | Added a play session and viewed profile. | Play session statistic increases. | Pass | Confirms profile stats use related play session data. |
| T077 | Game detail route | Clicked a game title from the games table. | Game detail page opens. | Pass | Confirms detail route and clickable title are connected. |
| T078 | Game detail information | Viewed a saved game's detail page. | Game information and image display correctly. | Pass | Confirms detail template displays saved model fields. |
| T079 | Play session history | Viewed detail page for a game with a play session. | Play session appears in the history panel. | Pass | Confirms related play sessions display under the correct game. |
| T080 | Empty play session history | Viewed detail page for a game with no play sessions. | Empty session message displays. | Pass | Confirms detail page handles games without sessions. |
| T081 | Detail page action links | Used Add Session, Edit Game, Delete Game and Back to Games buttons from detail page. | Each link opens the correct page. | Pass | Confirms detail page navigation works. |
| T082 | PremiumAccess model setup | Added `PremiumAccess` model and ran `python manage.py check`. | Django reports no system check issues. | Pass | Confirms premium access can be stored per user. |
| T083 | PremiumAccess migration | Ran `python manage.py makemigrations` and `python manage.py migrate`. | PremiumAccess table is created successfully. | Pass | Confirms premium model was added to the database. |
| T084 | Premium admin setup | Registered `PremiumAccess` in Django admin and ran checks. | Django reports no admin configuration issues. | Pass | Premium records can be managed through admin if needed. |
| T085 | Premium route protection | Visited `/checkout/premium/` while logged out. | User is redirected to login. | Pass | Confirms premium page requires authentication. |
| T086 | Premium locked state | Viewed premium page while logged in without premium access. | Premium locked content displays. | Pass | Confirms free users cannot see unlocked premium content. |
| T087 | Premium navbar link | Clicked `PREMIUM` in the authenticated navbar. | Premium page opens. | Pass | Confirms navbar link is connected. |
| T088 | Stripe package install | Installed `stripe` and updated `requirements.txt`. | Stripe package is available to the project. | Pass | Required for Stripe Checkout integration. |
| T089 | Stripe settings | Added Stripe environment variable settings and ran `python manage.py check`. | Django reports no system check issues. | Pass | Secret keys are read from environment variables, not hard-coded. |
| T090 | Checkout session creation | Clicked `Unlock Premium` while logged in with Stripe keys configured. | User is redirected to Stripe Checkout. | Pass | Confirms server creates a Stripe Checkout Session. |
| T091 | Successful premium payment | Completed Stripe test payment using test card `4242 4242 4242 4242`. | User returns to GameShelf and premium access is unlocked. | Pass | `PremiumAccess` is created/updated after verifying Stripe session payment status. |
| T092 | Premium unlocked state | Viewed premium page after payment. | Premium unlocked content displays. | Pass | Confirms paid users see premium content. |
| T093 | Cancelled Stripe payment | Started checkout and cancelled before payment. | User returns to premium page with cancellation message. | Pass | Confirms cancelled payment does not unlock premium. |
| T094 | Premium context processor | Added premium context processor and ran `python manage.py check`. | Django reports no system check issues. | Pass | Templates can access premium status globally. |
| T095 | Premium navbar badge | Logged in as a premium user. | Navbar displays `GAMESHELF PREMIUM`. | Pass | Confirms premium status changes the shared layout. |
| T096 | Premium navbar styling | Logged in as a premium user. | Navbar displays premium visual styling. | Pass | Confirms paid users receive a visible premium state. |
| T097 | Premium profile tier | Viewed profile as a premium user. | Account tier displays as Premium. | Pass | Confirms profile uses premium access status. |
| T098 | Free user visual state | Logged in as a non-premium user. | Navbar has no premium badge and profile tier displays Free. | Pass | Confirms premium UI is only shown to paid users. |
| T099 | Homepage start button | Clicked `Start your shelf` as logged-out and logged-in user. | Logged-out users go to register; logged-in users go to games list. | Pass | Replaced placeholder `#` link with real navigation. |
| T100 | Visual polish pass | Replaced CSS with a polished theme and checked main pages. | Pages keep existing functionality while displaying improved styling. | Pass | Visual design now uses stronger spacing, shadows and consistent panels. |
| T101 | Responsive visual check | Reduced browser width and checked homepage, games page and profile. | Layout stacks cleanly on smaller screens. | Pass | Confirms updated responsive CSS works across main layouts. |
| T102 | Mobile navbar | Viewed app below 800px width and clicked hamburger button. | Navigation opens vertically without wrapping onto multiple header lines. | Pass | Added custom JavaScript toggle for mobile navigation. |
| T103 | Mobile games layout | Viewed games page below 900px width. | Filter panel and games table fit inside the screen layout. | Pass | Prevents page content from overflowing off-screen. |
| T104 | Removed unwanted gradients | Viewed homepage and profile after CSS updates. | Hero, profile avatar and stat cards use flat surface styling. | Pass | Visual design better matches preferred style. |
| T105 | Filter collapse control | Viewed games page below 900px width and used Show more/less filters. | Filter section expands and collapses correctly. | Pass | Collapse control only appears on smaller layouts. |
| T106 | Favourites checkbox alignment | Viewed games filter form below 800px width. | Checkbox and label remain aligned together. | Pass | Replaced label-wrapped checkbox with a dedicated checkbox row. |
| T107 | Premium mobile dropdown styling | Opened mobile navbar as a premium user. | Dropdown matches the premium navbar styling. | Pass | Premium users keep consistent visual state on mobile. |
| T108 | Mobile table columns | Viewed games table below 800px width. | Less important columns are hidden and actions remain accessible. | Pass | Mobile table prioritises image, title, platform and actions. |
| T109 | Template accessibility cleanup | Reviewed base, games list and game form templates. | Navigation, table headers and form side panel include clearer accessible markup. | Pass | Added hamburger label, table header scopes and form-side `aria-label`. |
| T110 | Hide borrowed/sold filter | Ticked `Hide borrowed/sold` and applied filters. | Borrowed and sold games are hidden from the games table. | Pass | Confirms custom exclusion filter works. |
| T111 | Clear hide unavailable filter | Clicked `Clear filters` after hiding borrowed/sold games. | Full games list displays again. | Pass | Confirms filter state can be reset. |
| T112 | Multiple platform badge picker | Clicked multiple platform badges on the Add Game form. | Platform field is filled with comma-separated selected platforms. | Pass | Allows users to record games owned on more than one platform. |
| T113 | Platform badge toggle | Clicked a selected platform badge again. | Platform is removed from the platform field and visual selection clears. | Pass | Confirms users can correct badge selections. |
| T114 | Manual custom platform | Typed a custom platform manually into the platform field. | Custom platform saves successfully. | Pass | Supports platforms not included in the badge list. |
| T115 | Edit existing platform badges | Opened edit page for a game with saved platforms. | Matching platform badges show as selected. | Pass | Confirms saved platform text syncs with badge UI. |
| T116 | Custom platform entry | Typed a platform manually into the platform field. | Custom platform text remains saved after submitting the form. | Pass | Supports platforms not included in the badge list, such as older consoles. |
| T117 | Favourite star control | Ticked and unticked the favourite star on the game form. | Star changes visual state and saved favourite status updates correctly. | Pass | Replaced the standard checkbox with a clearer star-style control. |
| T118 | Game image upload panel | Viewed the image upload section on add and edit game pages. | Current image, upload control and preview are spaced clearly inside the side panel. | Pass | Improves form usability and visual layout. |
| T119 | Remove image control | Clicked Remove image on an existing uploaded game image and saved the form. | Uploaded image is removed from the game after saving. | Pass | Replaced Django's default clear checkbox with a styled remove image button. |
| T120 | Registration email field | Created a new account with a username, email and password. | Account is created successfully and stores the email address. | Pass | Adds email support ready for password reset functionality. |
| T121 | Duplicate email validation | Tried to register another account using an email already linked to an existing user. | Form displays an error and prevents the duplicate email registration. | Pass | Prevents multiple accounts from sharing the same password reset email. |
| T122 | Registration form styling | Submitted the register form with a duplicate email address. | Error message displays in red and field labels are bold. | Pass | Improves readability of registration form validation. |
| T123 | Forgot password link | Clicked the forgotten password link on the login page. | Password reset page opens successfully. | Pass | Adds account recovery navigation. |
| T124 | Password reset form page | Submitted an email address on the reset password page. | User is redirected to the reset link sent confirmation page. | Pass | Uses temporary console email backend until real email is configured for deployment. |
| T125 | Password reset templates | Opened the password reset confirmation and complete templates through Django's auth flow. | Templates are available and styled consistently with other auth pages. | Pass | Full reset page structure is ready for deployment email setup. |
| T126 | Premium accent colour options | Viewed the Premium page as a premium user. | Accent colour options are displayed. | Pass | Confirms premium users can access visual customisation. |
| T127 | Accent colour update | Selected a new accent colour from the Premium page. | Success message appears and the site colour theme updates. | Pass | Confirms the selected colour is saved to the premium user record. |
| T128 | Premium visual state retained | Changed accent colour while logged in as a premium user. | Navbar still shows the premium badge and premium styling. | Pass | Confirms accent customisation does not remove the premium account state. |
| T129 | Accent colour readability | Checked each accent colour against buttons, cards and messages. | Text remains readable across available colour themes. | Pass | Confirms selected colours are usable for the interface. |