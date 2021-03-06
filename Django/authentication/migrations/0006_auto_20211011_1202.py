# Generated by Django 3.1.7 on 2021-10-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20211010_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='siteuser',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='role',
            field=models.PositiveIntegerField(choices=[(3, 'member'), (2, 'startup'), (1, 'admin')], default=3),
        ),
    ]
