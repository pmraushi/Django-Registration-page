# Generated by Django 3.2.7 on 2021-11-19 02:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('signup_app', '0002_rename_email_address_register_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
