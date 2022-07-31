from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinLengthValidator(18), MaxLengthValidator(35)])
    heart_rate = models.IntegerField(default=60, validators=[MinLengthValidator(60), MaxLengthValidator(150)])

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old, heart rate is {self.heart_rate}"
