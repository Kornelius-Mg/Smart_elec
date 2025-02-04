# Generated by Django 3.0.6 on 2020-07-11 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compteur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instant', models.DateTimeField(auto_now=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=11)),
                ('quantite', models.DecimalField(decimal_places=2, max_digits=11)),
                ('compteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compteur.Compteur')),
            ],
        ),
    ]
