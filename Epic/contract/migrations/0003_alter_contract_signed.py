# Generated by Django 4.1.3 on 2022-11-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_alter_contract_signed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='signed',
            field=models.BooleanField(default=False),
        ),
    ]