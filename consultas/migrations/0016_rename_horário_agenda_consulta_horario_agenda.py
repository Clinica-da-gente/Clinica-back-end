# Generated by Django 4.0.6 on 2022-07-21 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0015_remove_consulta_data_da_consulta_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='horário_agenda',
            new_name='horario_agenda',
        ),
    ]
