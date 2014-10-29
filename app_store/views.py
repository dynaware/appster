from django.shortcuts import render

from app_store.models import *


def index(request):
	return render(request, 'app_store/index.html', {'apps': Application.objects.all()})
