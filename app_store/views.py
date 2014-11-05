from django.shortcuts import render

from app_store.models import *


def index(request):
	return render(request, 'app_store/index.html', {'apps': Application.objects.all(), 'title': 'Appster by Dynaware'})


def detail(request, app_id):
	app = Application.objects.get(id=app_id)
	return render(request, 'app_store/detail.html', {'app': app, 'title': '{} | Appster'.format(app.name)})


def category(request, category_id):
	category = Category.objects.get(id=category_id)
	return render(
		request,
		'app_store/category.html',
		{
			'category': category,
			'apps': Application.objects.filter(category=category_id),
			'title': '{} | Appster'.format(category.title),
		}
	)


def categories(request):
	return render(
		request,
		'app_store/categories.html',
		{
			'categories': Category.objects.all(),
			'title': 'Browse Categories | Appster',
		}
	)
