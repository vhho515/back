# Generated by Django 3.0.7 on 2021-12-13 20:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]