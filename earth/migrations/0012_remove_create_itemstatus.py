# Generated by Django 3.2.9 on 2022-06-02 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0011_alter_create_benefactor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create',
            name='ItemStatus',
        ),
    ]
