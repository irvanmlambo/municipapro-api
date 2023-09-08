# Generated by Django 3.2.14 on 2022-11-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_state_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cycle',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='cycle',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
