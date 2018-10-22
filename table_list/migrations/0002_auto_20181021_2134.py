# Generated by Django 2.1.1 on 2018-10-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table_items',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='table_items',
            name='start_date',
            field=models.DateTimeField(default=None),
        ),
    ]