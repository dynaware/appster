from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from app_store.models import *
from appster import settings
from app_store import forms


def page_title(title):
	if settings.database == 'sqlite':
		return title + ' | DEBUG_DB'
	else:
		return title


def index(request):
	return render(
		request,
		'app_store/index.html',
		{
			'apps': sorted(Application.objects.filter(approved=True), key=lambda x: x.rating, reverse=True),
			'title': page_title('Appster by Dynaware'),
		}
	)


def detail(request, app_id):
	app = Application.objects.get(id=app_id)
	app.click_count += 1
	app.save()
	return render(
		request,
		'app_store/detail.html',
		{
			'app': app,
			'title': page_title('{} | Appster'.format(app.name)),
			'related_apps': sorted(
				Application.objects.filter(
					category=app.category.id,
				).exclude(
					id=app.id,
				)[:4],
				key=lambda x: x.rating, reverse=True
			),
		}
	)


def category(request, category_id):
	category = Category.objects.get(id=category_id)
	return render(
		request,
		'app_store/category.html',
		{
			'category': category,
			'apps': Application.objects.filter(category=category_id, approved=True),
			'title': page_title('{} | Appster'.format(category.title)),
		}
	)


def categories(request):
	return render(
		request,
		'app_store/categories.html',
		{
			'categories': Category.objects.all(),
			'title': page_title('Browse Categories | Appster'),
		}
	)


def search(request):
	query = request.GET.get('query', '')
	sort_key = request.GET.get('sort', '-rating')

	r = False
	if sort_key.startswith('-'):
		r = True

	if 'rating' in sort_key:
		k = lambda x: x.rating
	elif 'name' in sort_key:
		k = lambda x: x.name
	else:
		k = lambda x: x.rating

	return render(
		request,
		'app_store/search.html',
		{
			'results': sorted(Application.objects.filter(name__icontains=query, approved=True), key=k, reverse=r),
			'title': page_title('Search Results | Appster'),
			'query': query,
		}
	)


def app_lists(request):
	return render(
		request,
		'app_store/app_lists.html',
		{
			'lists': ApplicationList.objects.all(),
			'title': page_title('Application Lists | Appster'),
		}
	)


def app_list(request, list_id):
	list = ApplicationList.objects.get(id=list_id)
	return render(
		request,
		'app_store/app_list.html',
		{
			'app_list': list,
			'apps': [i.application for i in list.applicationlistentry_set.all()],
			'title': page_title('{} | Appster'.format(list.name)),
		}
	)


@login_required(login_url='/auth/login')
def new_review(request, app_id):
	app = Application.objects.get(id=app_id)
	form = forms.ReviewForm()
	if request.POST:
		review = Review(application=app, author=request.user)
		form = forms.ReviewForm(request.POST, instance=review)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('detail', args=(app_id,)))

	return render(
		request,
		'app_store/form.html',
		{
			'title': page_title('New Review | Appster'),
			'subtitle': app.name,
			'form_name': 'New Review',
			'form': form,
			'app': app,
			'url': reverse('new_review', args=(app_id,)),
		}
	)

@login_required(login_url='/auth/login')
def new_application(request):
	alert = None
	form = forms.NewApp()

	if request.POST:
		app = Application(approved=False)
		form = forms.NewApp(request.POST, instance=app)
		if form.is_valid():
			form.save()

		alert = 'Application was created successfully, Appster staff will review your request'

	return render(
		request,
		'app_store/form.html',
		{
			'title': page_title('Request New App | Appster'),
			'form_name': 'New Application Request',
			'form': form,
			'alert': alert,
			'url': reverse('new_app'),
		}
	)


@login_required(login_url='/auth/login')
def review_applications(request):
	if not request.user.is_staff:
		return index(request)

	return render(
		request,
		'app_store/review_apps.html',
		{
			'title': page_title('Review App Submissions | Appster'),
			'apps': Application.objects.filter(approved=False),
		}
	)

@login_required(login_url='/auth/login')
def review_application(request, app_id, choice):
	if not request.user.is_staff:
		return index(request)

	app = Application.objects.get(id=app_id)
	if choice == '0':
		app.delete()
	if choice == '1':
		app.approved = True
		app.save()

	return render(
		request,
		'app_store/review_apps.html',
		{
			'title': page_title('Review App Submissions | Appster'),
			'apps': Application.objects.filter(approved=False),
		}
	)


def about(request):
	return render(
		request,
		'app_store/about.html',
		{
			'title': page_title('About | Appster'),
		}
	)


@login_required(login_url='/auth/login')
def new_app_list_entry(request, app_id):
	form = forms.ApplicationListEntryForm()
	form.fields['list'].queryset = ApplicationList.objects.filter(author=request.user)
	alert = None
	app = Application.objects.get(id=app_id)

	if request.POST:
		list_entry = ApplicationListEntry(application=app)
		form = forms.ApplicationListEntryForm(request.POST, instance=list_entry)
		if form.is_valid():
			list_entry = form.save()
			return HttpResponseRedirect(reverse('app_list', args=(list_entry.list.id,)))


	return render(
		request,
		'app_store/form.html',
		{
			'title': page_title('Add App to List | Appster'),
			'subtitle': app.name,
			'form_name': 'Add App to List',
			'form': form,
			'alert': alert,
			'url': reverse('new_app_list_entry', args=(app_id,)),
		}
	)
