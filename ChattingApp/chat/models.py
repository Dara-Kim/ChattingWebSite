from django.db import models


class UserAccount(models.Model):
    user_id = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
