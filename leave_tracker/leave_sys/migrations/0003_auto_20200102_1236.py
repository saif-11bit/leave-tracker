# Generated by Django 3.0.1 on 2020-01-02 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leave_sys', '0002_holiday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holiday',
            old_name='from_to',
            new_name='to_date',
        ),
    ]
