# Generated by Django 4.0.3 on 2022-08-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_voterlist_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterlist',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='image/voterlist/'),
        ),
    ]
