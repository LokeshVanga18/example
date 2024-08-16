# Generated by Django 5.1 on 2024-08-14 07:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('name', models.CharField(max_length=20, unique=True)),
                ('std_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_num', models.BigIntegerField(unique=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hp.personalinfo')),
            ],
        ),
    ]
