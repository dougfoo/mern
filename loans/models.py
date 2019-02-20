from django.db import models

# Create your models here.


class Loan(models.Model):
    id = models.DecimalField(decimal_places=0, max_digits=12, primary_key=True)
    name = models.CharField(max_length=40)
    toEmail = models.CharField(max_length=60)  # should be selected
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    details = models.TextField()

    def __str__(self):
        return self.name + ' to ' + self.toEmail + ': ' + str(self.amount)
