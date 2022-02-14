from django.contrib import admin
from .models.category import Category
from .models.product import Product
from .models.customer import  Contact
#from .models.order import Orders
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from django.utils.html import format_html
from django.contrib import admin
from .models.product import Product, ReviewRating, ProductGallery
from .models.carts import Cart,CartItem
from .models.order import Payment,OrderProduct,Order
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')




class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')


#@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','customer_need', 'email', 'phone', 'create_date')
    #list_display_links = ('id', 'first_name', 'last_name')
    #search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline]

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
admin.site.register(Contact, ContactAdmin)
#admin.site.register(Variation)
admin.site.register(Product, ProductAdmin)

admin.site.register(ReviewRating)
admin.site.register(ProductGallery)

admin.site.register(Account, AccountAdmin)
#admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Category, CategoryAdmin)
