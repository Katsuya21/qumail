# Generated by Django 3.2.23 on 2023-12-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantserver', '0002_alter_users_salt'),
    ]

    operations = [
        migrations.AddField(
            model_name='emails',
            name='synced',
            field=models.BooleanField(default=False),
        ),
    ]
