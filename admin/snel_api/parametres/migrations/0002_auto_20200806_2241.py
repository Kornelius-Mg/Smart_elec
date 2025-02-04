# Generated by Django 3.0.6 on 2020-08-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametres', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClasseForfait',
        ),
        migrations.RemoveField(
            model_name='reglagesgeneral',
            name='alert_level',
        ),
        migrations.AddField(
            model_name='reglagesgeneral',
            name='min_alert_compteurs',
            field=models.IntegerField(default=75, verbose_name="Niveau d'alerte minimal des compteurs"),
        ),
        migrations.AddField(
            model_name='reglagesgeneral',
            name='min_alert_transfos',
            field=models.IntegerField(default=75, verbose_name="Niveau d'alerte minimal des transfos"),
        ),
        migrations.AlterField(
            model_name='reglagesgeneral',
            name='prix_par_watt',
            field=models.IntegerField(default=75, verbose_name='Prix du wattheure en francs congolais'),
        ),
    ]
