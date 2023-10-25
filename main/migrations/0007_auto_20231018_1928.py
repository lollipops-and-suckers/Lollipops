# Generated by Django 3.2.8 on 2023-10-18 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20231017_2352'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='skills',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]