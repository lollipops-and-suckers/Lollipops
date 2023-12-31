# Generated by Django 3.2.8 on 2023-10-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20231018_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.CharField(max_length=100, verbose_name='Profile:')),
                ('EMAIL_HOST', models.CharField(max_length=100, verbose_name='Email Host:')),
                ('EMAIL_HOST_USER', models.CharField(max_length=100, verbose_name='Email Host User:')),
                ('EMAIL_HOST_PASSWORD', models.CharField(max_length=100, verbose_name='Email Host Password:')),
                ('EMAIL_PORT', models.IntegerField(verbose_name='Email Port:')),
                ('EMAIL_USE_TLS', models.BooleanField(verbose_name='Email Use TLS:')),
                ('EMAIL_BACKEND', models.CharField(max_length=100, verbose_name='Email Backend:')),
            ],
            options={
                'verbose_name': 'Website Email Setting',
                'verbose_name_plural': 'Website Email Settings',
            },
        ),
    ]
