from django.contrib import admin

from order.models import Order, Order_Item


class Order_ItemInline(admin.TabularInline):
    model = Order_Item
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [Order_ItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Item)
