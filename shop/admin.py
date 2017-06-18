from django.contrib import admin
from .models import Category, Product
# qqqqqqqq

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}  # 使用name字段自动赋值


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'image',
                    'available', 'created','updated']
    list_filter = ['available', 'created', 'updated']
    search_fields = ('name',)
    list_editable = ['price', 'stock', 'available', 'image']   # 设置可以被编辑的字段，这样可以让你一次编辑多行，任何在 list_editable 的字段也必须在 list_display 中，因为只有这样被展示的字段才可以被编辑。
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)