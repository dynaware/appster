from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from app_store.views import page_title
from app_store.models import ApplicationList
from user_auth import forms


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

				if request.POST.get('next'):
					next = request.POST.get('next')
					return HttpResponseRedirect(next)


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
			'title': page_title('Login | Appster'),
			'next': request.GET.get('next')
		}
	)


def logout_user(request):
	logout(request)
	return login_user(request)


def register_user(request):
	if request.POST:
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		return render(
			request,
			'user_auth/signup.html',
			{
				'form': UserCreationForm,
				'title': page_title('Signup | Appster'),
			}
		)


@login_required(login_url='/auth/login')
def user(request):
	lists = ApplicationList.objects.filter(author=request.user)
	return render(
		request,
		'user_auth/user.html',
		{
			'title': page_title('Your Account | Appster'),
			'lists': lists,
		}
	)


@login_required(login_url='/auth/login')
def app_list(request):
	form = forms.AppListForm()

	if request.POST:
		app_list = ApplicationList(author=request.user)
		form = forms.AppListForm(request.POST, instance=app_list)
		if form.is_valid():
			form.save()

			return user(request)
		else:
			form = forms.AppListForm()


	return render(
		request,
		'app_store/form.html',
		{
			'title': page_title('New App List | Appster'),
			'form': form,
			'form_name': 'New App List',
			'url': '/auth/app_list'
		}
	)
