from django.contrib import admin

from .models import MenuItem, Category, OrderModel
from .views import Order

# Register your models here.
#admin.site.register(MenuItem)
admin.site.register(Category)
#admin.site.register(OrderModel)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price')
    ordering = ('id',)
    search_fields = ('name', 'price')
    list_filter = ('category',)

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'address','is_delivery')
    list_filter = ('is_delivery',)
    ordering = ('id',)
    search_fields = ('address','postcode')