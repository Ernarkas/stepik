from django.urls import path

from .views import get_week_day

urlpatterns = [

    path('<day>/', get_week_day),

]
