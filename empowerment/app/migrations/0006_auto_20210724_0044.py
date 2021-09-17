# Generated by Django 3.2.3 on 2021-07-23 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210720_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='eaddress',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='address',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='city',
        ),
        migrations.RemoveField(
            model_name='application',
            name='document',
        ),
        migrations.RemoveField(
            model_name='application',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='application',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='application',
            name='state',
        ),
        migrations.RemoveField(
            model_name='application',
            name='zip',
        ),
        migrations.AddField(
            model_name='application',
            name='subject',
            field=models.IntegerField(default=''),
        ),
    ]
