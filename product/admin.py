from django.contrib import admin
from product.models import Product, TestModel


# Register your models here.
class TestModelAdmin(admin.StackedInline):
    model = TestModel
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active', 'created', 'update')  # show fields in admin
    list_editable = ('active',)  # make a field aditable
    search_fields = ('title', 'body')
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TestModelAdmin]
