# Generated by Django 3.2.19 on 2023-07-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0035_auto_20230704_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='organization_size',
            field=models.CharField(max_length=20),
        ),
    ]
