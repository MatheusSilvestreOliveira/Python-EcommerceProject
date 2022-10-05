from django.contrib import admin
from product.models import Product, Variety


class VarietyInline(admin.TabularInline):
    model = Variety
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_name', 'prod_price', 'prod_description_short',)
    list_display_links = ('prod_name', 'prod_price',)
    inlines = [VarietyInline]


class VarietyAdmin(admin.ModelAdmin):
    list_display = ('variety_name', 'product', 'variety_price',)
    list_display_links = ('variety_name', 'product',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Variety, VarietyAdmin)
