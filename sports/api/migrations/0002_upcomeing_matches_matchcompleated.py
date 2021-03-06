# Generated by Django 4.0.4 on 2022-06-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcomeing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=50)),
                ('team2', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='matches',
            name='matchCompleated',
            field=models.BooleanField(default=False),
        ),
    ]
