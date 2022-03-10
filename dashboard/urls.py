from django.urls import path
from dashboard.views.category import admin_products_category,admin_add_category,admin_delete_category,admin_edit_category,category_search
from dashboard.views.home import admin_dashboard,admin_product_order,admin_serach
from dashboard.views.product import admin_add_product,admin_products_list,admin_product_delete,admin_edit_product
from dashboard.views.login import admin_login,admin_register,admin_logout,admin_edit_profile
urlpatterns =[
    path('',admin_dashboard,name="admin_dashboard"),
    #path('admin_category',views.admin_products_category,name ="admin_category"),
    path('admin_product_order',admin_product_order,name="admin_product_order"),
    path('admin_product_list',admin_products_list,name="admin_product_list"),
    path('admin_add_category',admin_add_category,name ="admin_add_category"),
    path('admin_products_category',admin_products_category,name ="admin_products_category"),

    path('admin_serach',admin_serach,name="admin_serach"),
    path('admin_delete_category/<int:category_id>/',admin_delete_category,name='admin_delete_category'),
    path('admin_edit_category/<int:category_id>/',admin_edit_category,name="admin_edit_category"),
    path('category_search',category_search,name="category_search"),
    # product add
    
    #
    
    path('admin_add_product', admin_add_product, name='admin_add_product'),
    path('admin_product_delete/<int:product_id>/',admin_product_delete,name="admin_product_delete"),
    path('admin_edit_product/<int:product_id>/',admin_edit_product,name="admin_edit_product"),
    # admin_profile
    path('admin_register',admin_register,name="admin_register"),
    path('admin_login/',admin_login,name ='admin_login'),
    path('admin_logout',admin_logout,name="admin_logout"),
    path('admin_edit_profile',admin_edit_profile,name="admin_edit_profile"),






]