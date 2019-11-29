# Generated by Django 2.0.8 on 2018-08-14 14:02

import account.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username')),
                ('nickname', models.CharField(max_length=30, unique=True, verbose_name='Nickname')),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='account/%Y/%m/%d', verbose_name='Nickname')),
                ('in_short', models.CharField(blank=True, default='작성한 한마디가 없습니다.', max_length=255, verbose_name='In short')),
                ('level', models.IntegerField(default=1, verbose_name='In short')),
                ('code', models.CharField(default='Z0', max_length=30, verbose_name='code')),
                ('exp', models.IntegerField(default=0, verbose_name='In short')),
                ('point', models.IntegerField(default=0, verbose_name='Point')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-date_joined',),
            },
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Phone Number')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
            ],
        ),
    ]
