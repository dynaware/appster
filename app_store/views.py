from django.shortcuts import render

from app_store.models import *
from appster import settings


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
			'title': page_title('Appster by Dynaware')
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
			'apps': Application.objects.filter(category=category_id),
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
	return render(
		request,
		'app_store/search.html',
		{
			'results': Application.objects.filter(name__icontains=query),
			'title': page_title('Search Results | Appster'),
		}
	)
