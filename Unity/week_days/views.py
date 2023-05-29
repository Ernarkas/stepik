from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound



def get_week_day(request, day):
    if day == 'monday':
        return HttpResponse('Список дел на понедельник')
    elif day == 'tuesday':
        return HttpResponse('Список дел на вторнык')
    else:
        return HttpResponseNotFound(f'{day} - такого дня бывить!')