# Generated by Django 4.1.6 on 2023-03-06 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_image', models.ImageField(upload_to='product_image')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.category')),
            ],
        ),
    ]
