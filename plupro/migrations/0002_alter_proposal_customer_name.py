# Generated by Django 3.2.4 on 2021-06-23 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plupro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='customer_name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
