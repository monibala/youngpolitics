# Generated by Django 4.0.3 on 2022-08-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_elec_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='elec_res',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
