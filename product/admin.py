from django.contrib import admin
from product.models import Category, Product, Images

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','image_tag','status']
    list_filter=['status']
    readonly_fields = ('image_tag',)

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','image_tag','price', 'quantity', 'status','image']
    list_filter=['status']
    inlines = [ProductImageInline]
    readonly_fields = ('image_tag',)

class ImagesAdmin(admin.ModelAdmin):
    list_display=['title','image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Images,ImagesAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
# Register your models here.
