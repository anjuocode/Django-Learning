# Generated by Django 4.0 on 2022-01-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Marks', models.IntegerField()),
            ],
        ),
    ]