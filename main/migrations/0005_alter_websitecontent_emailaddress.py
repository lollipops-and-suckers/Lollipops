# Generated by Django 3.2.8 on 2023-10-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_websitecontent_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitecontent',
            name='emailAddress',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
    ]
