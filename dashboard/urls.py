from django.urls import path
from dashboard.views.category import admin_add_category,admin_products_category,admin_edit_category
from dashboard.views.home import admin_dashboard,admin_product_order,admin_serach
from dashboard.views.product import admin_form_product,admin_product_grid,admin_product_add,admin_add_product_view,admin_products_list
from dashboard.views.login import admin_login,admin_register
urlpatterns =[
    path('',admin_dashboard,name="admin_dashboard"),
    #path('admin_category',views.admin_products_category,name ="admin_category"),
    path('admin_product_order',admin_product_order,name="admin_product_order"),
    path('admin_product_list',admin_products_list,name="admin_product_list"),
    path('admin_form_product',admin_form_product,name ="admin_form_product"),
    path('admin_add_category',admin_add_category,name ="admin_add_category"),
    path('admin_products_category',admin_products_category,name ="admin_products_category"),
    path('admin_register',admin_register,name="admin_register"),
    path('admin_login',admin_login,name ='admin_login'),
    path('admin_serach',admin_serach,name="admin_serach"),
    path('admin_product_grid',admin_product_grid,name="admin_product_grid"),
    #path('admin_product_add/<int:product_id>/',admin_product_add,name="admin_product_add"),
    #path('admin_add_product_view',admin_add_product_view,name ="admin_add_product_view"),
    path('admin_product_add', admin_product_add, name='admin_product_add'),
    path('admin_edit_category/<slug:category_slug>/',admin_edit_category,name='admin_edit_category'),



]