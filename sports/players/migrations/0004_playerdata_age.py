# Generated by Django 4.0.3 on 2022-03-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_playerdata_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerdata',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
