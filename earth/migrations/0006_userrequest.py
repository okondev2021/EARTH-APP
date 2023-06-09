# Generated by Django 3.2.9 on 2022-05-27 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0005_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProofPic1', models.ImageField(null=True, upload_to='images/')),
                ('ProofPic2', models.ImageField(null=True, upload_to='images/')),
                ('RequestStatus', models.BooleanField(default=False)),
                ('About', models.CharField(max_length=3000)),
                ('Account', models.IntegerField()),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
