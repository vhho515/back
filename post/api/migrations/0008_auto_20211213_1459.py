# Generated by Django 3.0.7 on 2021-12-13 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cell_phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='zipcode',
        ),
    ]