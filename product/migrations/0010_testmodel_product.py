# Generated by Django 3.2 on 2022-11-21 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20221121_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول'),
        ),
    ]
