# Generated by Django 3.1.6 on 2021-05-15 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0033_auto_20210515_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endpoint',
            old_name='matched_gf',
            new_name='matched_patterns',
        ),
    ]
