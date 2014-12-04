from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
			'apps': sorted(Application.objects.all(), key=lambda x: x.rating, reverse=True),
			'title': page_title('Appster by Dynaware'),
			'logged_in': request.user.is_authenticated(),
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
			'logged_in': request.user.is_authenticated(),
		}
	)


def category(request, category_id):
	category = Category.objects.get(id=category_id)
	return render(
		request,
		'app_store/category.html',
		{
			'category': category,
			'apps': Application.objects.filter(category=category_id),
			'title': page_title('{} | Appster'.format(category.title)),
			'logged_in': request.user.is_authenticated(),
		}
	)


def categories(request):
	return render(
		request,
		'app_store/categories.html',
		{
			'categories': Category.objects.all(),
			'title': page_title('Browse Categories | Appster'),
			'logged_in': request.user.is_authenticated(),
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
			'results': sorted(Application.objects.filter(name__icontains=query), key=k, reverse=r),
			'title': page_title('Search Results | Appster'),
			'query': query,
			'logged_in': request.user.is_authenticated(),
		}
	)


def app_lists(request):
	return render(
		request,
		'app_store/app_lists.html',
		{
			'lists': ApplicationList.objects.all(),
			'title': page_title('Application Lists | Appster'),
			'logged_in': request.user.is_authenticated(),
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
			'logged_in': request.user.is_authenticated(),
		}
	)


@login_required(login_url='/auth/login')
def new_review(request, app_id):
	app = Application.objects.get(id=app_id)
	if request.POST:
		review = Review(application=app, author=request.user)
		form = forms.ReviewForm(request.POST, instance=review)
		form.save()

		return detail(request, app_id)

	return render(
		request,
		'app_store/new_review.html',
		{
			'title': page_title('New Review | Appster'),
			'logged_in': request.user.is_authenticated(),
			'form': forms.ReviewForm,
			'app': app,
		}
	)
