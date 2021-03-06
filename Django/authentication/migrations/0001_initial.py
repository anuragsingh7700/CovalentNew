# Generated by Django 3.1.7 on 2021-10-10 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Public Identifier')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.PositiveIntegerField(choices=[(1, 'admin'), (3, 'member'), (2, 'startup')], default=3)),
                ('contact_number', models.PositiveIntegerField(blank=True, default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('joining_date', models.CharField(default=django.utils.timezone.now, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gstin', models.CharField(max_length=15, unique=True)),
                ('pan', models.CharField(blank=True, max_length=16)),
                ('company_name', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=2048)),
                ('location', models.CharField(max_length=1024)),
                ('date_of_creation', models.DateField(default=django.utils.timezone.now)),
                ('industry', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('team_size', models.IntegerField(default=1)),
                ('website', models.URLField(blank=True, max_length=512)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='startup_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('review', models.TextField(max_length=1024)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.member')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.startup')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=15)),
                ('ifsc', models.CharField(max_length=10)),
                ('account_holders_name', models.CharField(max_length=128)),
                ('upi_id', models.CharField(max_length=256)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.startup')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='authentication.startup'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
