# Generated by Django 3.0.6 on 2020-06-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200627_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compteur',
            name='global_state',
            field=models.CharField(choices=[('OFF', 'Eteint'), ('ON', 'Allumé')], default='OFF', max_length=10),
        ),
        migrations.AlterField(
            model_name='transformateur',
            name='global_state',
            field=models.CharField(choices=[('OFF', 'OFF'), ('ON', 'ON')], default='OFF', max_length=10),
        ),
    ]
