# Generated by Django 3.1.2 on 2020-10-15 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201015_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='url',
            field=models.URLField(max_length=250),
        ),
    ]