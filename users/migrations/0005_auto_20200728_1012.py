# Generated by Django 3.0.8 on 2020-07-28 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200728_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='emailverified',
            new_name='is_active',
        ),
    ]