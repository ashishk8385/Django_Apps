# Generated by Django 4.1.7 on 2023-02-25 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_orderdetail_customer_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='customer_email',
            new_name='customer_name',
        ),
    ]
