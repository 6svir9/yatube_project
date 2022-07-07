# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, any_slug):
    return HttpResponse('Список публикаций')