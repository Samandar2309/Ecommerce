from django.contrib import admin
from .models import Product, Product_Images, Category, Contact, SubCategory, Social_links, Tags, Ads, Order


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    filter_horizontal = ('tags', 'product_images')
    list_filter = ('name', 'price')
    search_fields = ('id', 'name')


admin.site.register(Order)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Social_links)
admin.site.register(Tags)
admin.site.register(Ads)
admin.site.register(Contact)
admin.site.register(Product_Images)
