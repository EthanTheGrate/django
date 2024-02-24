from django.db import models

# Create your models here.
class food(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 10)
    place = models.CharField(max_length = 25)
    isveg = models.BooleanField(default = False)

    def __str__(self):
        return self.name