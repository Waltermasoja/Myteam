from django.db import models

class Members(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

