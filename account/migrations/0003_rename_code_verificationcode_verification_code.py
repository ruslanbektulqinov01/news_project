# Generated by Django 5.0.3 on 2024-05-02 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_verificationcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verificationcode',
            old_name='code',
            new_name='verification_code',
        ),
    ]
