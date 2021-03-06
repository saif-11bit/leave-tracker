# Generated by Django 3.0.1 on 2020-01-02 05:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(default=datetime.datetime.today)),
                ('to_date', models.DateField(default=datetime.datetime.today)),
                ('team_email', models.CharField(max_length=100)),
                ('reason', models.TextField()),
                ('leave_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave_sys.LeaveType')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave_sys.Staff')),
            ],
        ),
    ]
