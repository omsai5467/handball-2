# Generated by Django 4.0.4 on 2022-06-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_pointstable'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomeing',
            name='dis',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]