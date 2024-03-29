# Generated by Django 4.2.9 on 2024-01-15 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_address', models.CharField(max_length=200)),
                ('emp_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('emp_designation', models.CharField(max_length=50)),
            ],
        ),
    ]
