# Generated by Django 3.1.7 on 2021-10-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='q1',
            field=models.CharField(blank=True, default='', max_length=512, verbose_name='Question 1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='q2',
            field=models.CharField(blank=True, default='', max_length=512, verbose_name='Question 1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='q3',
            field=models.CharField(blank=True, default='', max_length=512, verbose_name='Question 1'),
        ),
    ]
