# Generated by Django 3.1.7 on 2021-10-11 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20211011_1203'),
        ('job', '0002_auto_20211010_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.member')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.project')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.startup')),
            ],
        ),
    ]