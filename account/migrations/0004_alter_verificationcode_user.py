# Generated by Django 5.0.3 on 2024-05-02 08:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_code_verificationcode_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
