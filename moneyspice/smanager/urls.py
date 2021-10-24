from django.urls import path

from .views import index, get_expense


urlpatterns = [
    path('', index, name='index'),
    path('show-expense/', get_expense, name='show-expense'),
]
