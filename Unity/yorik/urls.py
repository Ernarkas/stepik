from django.urls import path

from .views import get_zodiac_info

urlpatterns = [

    # path('leo/', leo),
    # path('capricon/', capricon),
    # path('taurus/', taurus),
    path('<sign_zodiac>/', get_zodiac_info),

]
