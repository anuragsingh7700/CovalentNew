# Generated by Django 3.1.7 on 2021-10-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20211011_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='role',
            field=models.PositiveIntegerField(choices=[(3, 'member'), (1, 'admin'), (2, 'startup')], default=3),
        ),
    ]