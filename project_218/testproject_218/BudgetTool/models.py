from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.title
