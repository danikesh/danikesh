# Generated by Django 3.2.3 on 2021-07-20 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_application_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='document',
            field=models.FileField(default=django.utils.timezone.now, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
