# Generated by Django 5.1 on 2024-10-29 01:43

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_remove_usuario_bairro_remove_usuario_cep_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.usuario')),
                ('especialidade', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
            bases=('usuario.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
