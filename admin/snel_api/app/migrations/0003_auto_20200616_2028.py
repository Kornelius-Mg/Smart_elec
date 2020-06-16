# Generated by Django 3.0.6 on 2020-06-16 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200616_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsCompteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instant', models.DateTimeField(auto_now=True)),
                ('i_phase1', models.FloatField(default=0)),
                ('i_phase2', models.FloatField(default=0)),
                ('i_phase3', models.FloatField(default=0)),
                ('u_phase1', models.FloatField(default=0)),
                ('u_phase2', models.FloatField(default=0)),
                ('u_phase3', models.FloatField(default=0)),
                ('p_phase1', models.FloatField(default=0)),
                ('p_phase2', models.FloatField(default=0)),
                ('p_phase3', models.FloatField(default=0)),
                ('q_phase1', models.FloatField(default=0)),
                ('q_phase2', models.FloatField(default=0)),
                ('q_phase3', models.FloatField(default=0)),
                ('etat', models.CharField(max_length=45)),
                ('compteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Compteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetailsTransfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instant', models.DateTimeField(auto_now=True)),
                ('i_phase1', models.FloatField(default=0)),
                ('i_phase2', models.FloatField(default=0)),
                ('i_phase3', models.FloatField(default=0)),
                ('u_phase1', models.FloatField(default=0)),
                ('u_phase2', models.FloatField(default=0)),
                ('u_phase3', models.FloatField(default=0)),
                ('p_phase1', models.FloatField(default=0)),
                ('p_phase2', models.FloatField(default=0)),
                ('p_phase3', models.FloatField(default=0)),
                ('q_phase1', models.FloatField(default=0)),
                ('q_phase2', models.FloatField(default=0)),
                ('q_phase3', models.FloatField(default=0)),
                ('etat', models.CharField(max_length=45)),
                ('transformateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Transformateur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Details_Compteur',
        ),
    ]
