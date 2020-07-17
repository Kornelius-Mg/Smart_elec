# Generated by Django 3.0.6 on 2020-07-17 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compteur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instant', models.DateTimeField(auto_now=True)),
                ('quantite', models.DecimalField(decimal_places=2, max_digits=11)),
                ('destinataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='compteur.Compteur')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='compteur.Compteur')),
            ],
        ),
    ]
