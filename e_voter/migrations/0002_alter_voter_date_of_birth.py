# Generated by Django 4.2.1 on 2023-05-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_voter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
