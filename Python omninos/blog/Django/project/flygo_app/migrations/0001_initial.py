# Generated by Django 4.0 on 2022-02-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
                ('Departure', models.DateField()),
                ('Return', models.DateField()),
                ('Name', models.CharField(max_length=30)),
                ('Mobile', models.IntegerField()),
            ],
        ),
    ]
