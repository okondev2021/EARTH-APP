# Generated by Django 3.2.9 on 2022-06-08 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0016_auto_20220608_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='Goal',
            field=models.IntegerField(default=0),
        ),
    ]
