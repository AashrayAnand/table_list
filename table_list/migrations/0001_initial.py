# Generated by Django 2.1.1 on 2018-10-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table_items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.TextField(default='')),
                ('date', models.DateTimeField(default=None)),
                ('day_of_week', models.TextField(default='')),
            ],
        ),
    ]
