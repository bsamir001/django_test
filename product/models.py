from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=20 , verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ',max_length=30, null=True, blank=True, allow_unicode=True)
    price = models.FloatField(verbose_name='قیمت')
    body = models.TextField(verbose_name='توضیحات')
    count = models.IntegerField(verbose_name='تعداد',null=True, blank=True)
    active = models.BooleanField(default=False , verbose_name='فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    update = models.DateTimeField(auto_now=True , verbose_name='زمان اپدیت')
    publish = models.DateTimeField(verbose_name='زمان انتشار' )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ('-created',)

class TestModel(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='محصول')#CASCADE:پاک شده همه , #SET_NULL:پاک کردن فقط ویژگی ها , #PROTECT : اجازه حذف کردن را نمیدهد
    title = models.CharField(max_length=20,verbose_name='عنوان')
    body = models.TextField(verbose_name='توضیحات')
    created = models.DateTimeField(auto_now_add=True,verbose_name='زمان ساخت')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'TestModel'
        verbose_name = 'تست'
        verbose_name_plural = ' تست ها'
        ordering = ('-created',)