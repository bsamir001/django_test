from django.urls import path
from product.views import category_view, product_details_view, checkout_view, cart_view, blog_view, blog_details_view, \
    tracking_view, elements_view, contact_view

app_name = 'product'
urlpatterns = [
    path('categody/', category_view, name='category_view'),
    path('detail/', product_details_view, name='product_details_view'),
    path('checkout/', checkout_view, name='checkout_view'),
    path('cart/', cart_view, name='cart_view'),
    path('blog/', blog_view, name='blog_view'),
    path('blog_details/', blog_details_view, name='blog_details_view'),
    path('tracking/', tracking_view, name='tracking_view'),
    path('elements/', elements_view, name='elements_view'),
    path('contact/', contact_view, name='contact_view'),
]
