# Generated by Django 3.2 on 2022-11-21 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_testmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-created',), 'verbose_name': 'تست', 'verbose_name_plural': ' تست ها'},
        ),
        migrations.RenameField(
            model_name='testmodel',
            old_name='cerated',
            new_name='created',
        ),
        migrations.AlterModelTable(
            name='testmodel',
            table='TestModel',
        ),
    ]
