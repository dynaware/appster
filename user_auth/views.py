from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from app_store.views import page_title


def login_user(request):
	state = 'Please log in below...'
	alert_level = ''
	username = ''
	logged_in = False

	if request.user.is_authenticated():
		state = 'You are already logged in'
		alert_level = 'success'
		logged_in = True

	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = 'You\'re successfully logged in!'
				alert_level = 'success'
				logged_in = True
			else:
				state = 'Your account is not active, please contact the site admin.'
				alert_level = 'warn'
		else:
			state = 'Your username and/or password were incorrect.'
			alert_level = 'alert'

	return render(
		request,
		'user_auth/login.html',
		{
			'state': state,
			'username': username,
			'alert_level': alert_level,
			'logged_in': logged_in,
			'title': page_title('Login | Appster'),
			'staff': request.user.is_staff,
		}
	)


def logout_user(request):
	logout(request)
	return login_user(request)
