from django.db import models

# Create your models here.
class table_items(models.Model):
    item_id = models.AutoField(primary_key=True)
    location = models.TextField(default='')
    date = models.DateTimeField(default=None)
    day_of_week = models.TextField(default='')
