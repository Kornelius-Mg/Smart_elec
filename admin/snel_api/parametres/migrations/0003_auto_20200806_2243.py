# Generated by Django 3.0.6 on 2020-08-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0002_auto_20200806_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reglagesgeneral',
            name='min_alert_compteurs',
            field=models.IntegerField(default=5, verbose_name="Niveau d'alerte minimal des compteurs"),
        ),
        migrations.AlterField(
            model_name='reglagesgeneral',
            name='min_alert_transfos',
            field=models.IntegerField(default=85, verbose_name="Niveau d'alerte minimal des transfos"),
        ),
        migrations.AlterField(
            model_name='reglagesgeneral',
            name='prix_par_watt',
            field=models.IntegerField(default=100, verbose_name='Prix du wattheure en francs congolais'),
        ),
    ]