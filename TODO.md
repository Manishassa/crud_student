# TODO: Modify Django App Flow

- [x] Add home view in views.py that redirects to student_list if authenticated, else to signup
- [x] Modify signup_view: remove auto-login, redirect to login after signup
- [x] Modify login_view: add check if already authenticated, redirect to student_list
- [x] Modify logout_view: redirect to home instead of student_list
- [x] Update urls.py: change root URL from student_list to home
