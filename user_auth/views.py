from django.shortcuts import render
from django.contrib.auth import authenticate, login


def login_user(request):
	state = 'Please log in below...'
	alert_level = ''
	username = ''
	if request.user:
		if request.user.is_authenticated():
			state = 'You are already logged in'
			alert_level = 'success'

	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = 'You\'re successfully logged in!'
				alert_level = 'success'
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
		}
	)
