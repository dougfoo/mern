from django.db import models

# Create your models here.


class Customer(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    mobile = models.CharField(max_length=60)
    myinfo = models.TextField()

    def __str__(self):
        return self.lname + ', ' + self.fname
