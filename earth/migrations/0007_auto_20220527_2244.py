# Generated by Django 3.2.9 on 2022-05-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0006_userrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrequest',
            old_name='Account',
            new_name='Amount',
        ),
        migrations.AddField(
            model_name='userrequest',
            name='Donation',
            field=models.IntegerField(default=0),
        ),
    ]
