# Generated by Django 3.1.2 on 2020-11-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0004_profile_neighbourhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='location',
            field=models.CharField(default='Nairobi', max_length=120),
        ),
    ]
