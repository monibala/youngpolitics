# Generated by Django 4.0.3 on 2022-08-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='fname',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='lname',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
    ]
