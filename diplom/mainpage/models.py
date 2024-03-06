from django.db import models

class MyClient(models.Model):
    name = models.CharField(max_length=64)
    phone = models.IntegerField()
    tgid = models.IntegerField(null=True)