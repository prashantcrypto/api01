from django.db import models

# Create your models here.


class user_data(models.Model):
    wallet_address = models.CharField(max_length=50, primary_key=True)
    twitter_link = models.CharField(max_length=200, null=True, blank=True)
