# Generated by Django 3.1.7 on 2021-03-31 23:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('registration_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=12)),
                ('company_email', models.EmailField(max_length=254)),
                ('date_of_creation', models.DateField(default=django.utils.timezone.now)),
                ('industry', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('company_code', models.PositiveIntegerField(unique=True, verbose_name='KTFSYTI')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('job_title', models.CharField(max_length=50)),
                ('joining_date', models.CharField(default=django.utils.timezone.now, max_length=50)),
                ('joining_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.startup')),
            ],
        ),
    ]