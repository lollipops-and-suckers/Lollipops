# Generated by Django 3.2.8 on 2023-10-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_websitecontent_websiteurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitecontent',
            name='websiteURL',
            field=models.CharField(default='#', max_length=200, verbose_name='Website URL'),
        ),
    ]
