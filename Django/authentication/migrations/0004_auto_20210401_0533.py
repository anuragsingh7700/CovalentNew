# Generated by Django 3.1.7 on 2021-04-01 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210401_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='company_code',
            field=models.PositiveIntegerField(default='FQGZHDH', unique=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='contact_no',
            field=models.CharField(max_length=10),
        ),
    ]
