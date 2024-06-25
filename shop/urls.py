from django.urls import path
from shop.views import home_page

app_name = 'shop'

urlpatterns = [
    path('', home_page, name='home_page'),
]
