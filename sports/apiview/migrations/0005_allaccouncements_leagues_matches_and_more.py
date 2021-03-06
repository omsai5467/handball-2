# Generated by Django 4.0.4 on 2022-05-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiview', '0004_athletescommission_boardmanagement_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='allaccouncements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='leagues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagueName', models.CharField(max_length=100)),
                ('fromStartDateToEndDate', models.CharField(max_length=100)),
                ('aboutLeague', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MatchName', models.CharField(blank=True, max_length=100)),
                ('StadiumName', models.CharField(blank=True, max_length=100)),
                ('MatchDate', models.CharField(blank=True, max_length=100)),
                ('team1', models.CharField(blank=True, max_length=100)),
                ('team2', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='athletescommission',
            name='state',
            field=models.CharField(choices=[('AndhraPradesh', 'AndhraPradesh'), ('ArunachalPradesh', 'ArunachalPradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'haryana'), ('HimachalPradesh', 'HimachalPradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('MadhyaPradesh', 'MadhyaPradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('TamilNadu', 'TamilNadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('UttarPradesh', 'UttarPradesh'), ('WestBengal', 'WestBengal'), ('AndamanAndNicobarIslands', 'AndamanAndNicobarIslands'), ('DaraAndNagar_HaveliAndDamanAndDiu', 'DaraAndNagar_HaveliAndDamanAndDiu'), ('lakshadweep', 'lakshadweep'), ('Delhi', 'Delhi'), ('ladakh', 'ladakh'), ('jammu_kashmir', 'jammu_kashmir')], max_length=100),
        ),
        migrations.AlterField(
            model_name='boardmanagement',
            name='state',
            field=models.CharField(choices=[('AndhraPradesh', 'AndhraPradesh'), ('ArunachalPradesh', 'ArunachalPradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'haryana'), ('HimachalPradesh', 'HimachalPradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('MadhyaPradesh', 'MadhyaPradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('TamilNadu', 'TamilNadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('UttarPradesh', 'UttarPradesh'), ('WestBengal', 'WestBengal'), ('AndamanAndNicobarIslands', 'AndamanAndNicobarIslands'), ('DaraAndNagar_HaveliAndDamanAndDiu', 'DaraAndNagar_HaveliAndDamanAndDiu'), ('lakshadweep', 'lakshadweep'), ('Delhi', 'Delhi'), ('ladakh', 'ladakh'), ('jammu_kashmir', 'jammu_kashmir')], max_length=100),
        ),
        migrations.AlterField(
            model_name='selectioncommittee',
            name='state',
            field=models.CharField(choices=[('AndhraPradesh', 'AndhraPradesh'), ('ArunachalPradesh', 'ArunachalPradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'haryana'), ('HimachalPradesh', 'HimachalPradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('MadhyaPradesh', 'MadhyaPradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('TamilNadu', 'TamilNadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('UttarPradesh', 'UttarPradesh'), ('WestBengal', 'WestBengal'), ('AndamanAndNicobarIslands', 'AndamanAndNicobarIslands'), ('DaraAndNagar_HaveliAndDamanAndDiu', 'DaraAndNagar_HaveliAndDamanAndDiu'), ('lakshadweep', 'lakshadweep'), ('Delhi', 'Delhi'), ('ladakh', 'ladakh'), ('jammu_kashmir', 'jammu_kashmir')], max_length=100),
        ),
        migrations.AlterField(
            model_name='stateassociations',
            name='state',
            field=models.CharField(choices=[('AndhraPradesh', 'AndhraPradesh'), ('ArunachalPradesh', 'ArunachalPradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'haryana'), ('HimachalPradesh', 'HimachalPradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('MadhyaPradesh', 'MadhyaPradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('TamilNadu', 'TamilNadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('UttarPradesh', 'UttarPradesh'), ('WestBengal', 'WestBengal'), ('AndamanAndNicobarIslands', 'AndamanAndNicobarIslands'), ('DaraAndNagar_HaveliAndDamanAndDiu', 'DaraAndNagar_HaveliAndDamanAndDiu'), ('lakshadweep', 'lakshadweep'), ('Delhi', 'Delhi'), ('ladakh', 'ladakh'), ('jammu_kashmir', 'jammu_kashmir')], max_length=200),
        ),
    ]
