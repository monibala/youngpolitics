# Generated by Django 4.0.3 on 2022-08-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.IntegerField()),
                ('service', models.CharField(choices=[('DM', 'Digital Marketing'), ('Vc', 'Voice Call'), ('Sms', 'Bulk Sms'), ('Ivr', 'IVR service'), ('App', 'Software/Mobile App')], max_length=100)),
            ],
        ),
    ]
