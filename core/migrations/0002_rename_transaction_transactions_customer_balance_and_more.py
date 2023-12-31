# Generated by Django 4.2.5 on 2023-09-18 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='Transactions',
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
