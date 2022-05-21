# Generated by Django 4.0.4 on 2022-05-21 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='playerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('fathername', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phonenumber', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('adhar', models.ImageField(blank=True, null=True, upload_to='aadhar/')),
                ('birth', models.ImageField(blank=True, null=True, upload_to='birth/')),
                ('playerid', models.CharField(blank=True, max_length=500000)),
                ('Height', models.CharField(blank=True, max_length=20, null=True)),
                ('Goals', models.CharField(blank=True, max_length=25, null=True)),
                ('Wins', models.CharField(blank=True, max_length=200, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('JersyNo', models.CharField(blank=True, max_length=20, null=True)),
                ('Weight', models.CharField(blank=True, max_length=100, null=True)),
                ('GamesNo', models.CharField(blank=True, max_length=500, null=True)),
                ('Losses', models.CharField(blank=True, max_length=500, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
