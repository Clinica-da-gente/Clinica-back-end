# Generated by Django 4.0.6 on 2022-07-15 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0013_alter_consulta_data_da_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data_da_consulta',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
