# Generated by Django 4.0.3 on 2022-08-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_my_team_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_team',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='image/team/images'),
        ),
    ]
