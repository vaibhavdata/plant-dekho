from django.urls import path
from .view.home import home
from .view.contact import contact
from .view.product import search,product,submit_review,product_detail,product_list
#from .view.order import OrderView
from .view.cart import cart,add_cart,remove_cart,remove_cart_item,checkout
from .view.order import payments,place_order
urlpatterns = [
    path('',home,name='home'),
    path('product/',product, name='product'),
    path('cart',cart,name='cart'),
    path('wishlist',cart, name ='wishlist'),
    path('product_list',product_list,name='product_list'),
    path('contact/', contact, name='contact'),
    path('search/',search, name='search'),
    path('category/<slug:category_slug>/', product, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('checkout/', checkout, name='checkout'),
    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', remove_cart_item, name='remove_cart_item'),
    path('place_order/', place_order, name='place_order'),
    path('payments/', payments, name='payments'),
    path('submit_review/<int:product_id>/', submit_review, name='submit_review'),
]