# Generated by Django 3.1.7 on 2021-10-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20211005_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='company_code',
            field=models.CharField(default='VOSLLHP', max_length=7, unique=True),
        ),
    ]