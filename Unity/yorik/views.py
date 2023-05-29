from django.http import HttpResponse, HttpResponseNotFound


def get_zodiac_info(request, sign_zodiac):
    if sign_zodiac == 'leo':
        return HttpResponse('Знак зодиака Лев')
    elif sign_zodiac == 'taurus':
        return HttpResponse('Знак зодиака Телец')
    elif sign_zodiac == 'capricon':
        return HttpResponse('Знак зодиака Козерог')
    else:
        return HttpResponseNotFound(f'Неизветсный знак зодиака - {sign_zodiac}')




