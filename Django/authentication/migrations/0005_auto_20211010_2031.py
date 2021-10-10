# Generated by Django 3.1.7 on 2021-10-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20211010_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='upi_id',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(help_text='0-bad to 5-excellent'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='role',
            field=models.PositiveIntegerField(choices=[(1, 'admin'), (2, 'startup'), (3, 'member')], default=3),
        ),
    ]