# Generated by Django 3.2.9 on 2022-06-04 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0014_alter_userrequest_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='Username',
            field=models.ForeignKey(limit_choices_to={'UserType': 'Receiver'}, on_delete=django.db.models.deletion.CASCADE, related_name='users_request', to=settings.AUTH_USER_MODEL),
        ),
    ]
