# Generated by Django 4.0.4 on 2022-06-01 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='pointsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
                ('PLD', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('LOSS', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
        ),
    ]
