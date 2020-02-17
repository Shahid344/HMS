from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.urls import reverse


Gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
     )

City = (
    ("Delhi", "Delhi"),
    ("Kolkata", "Kolkata"),
    ("Mumbai", "Mumbai"),
    ("Other", "Other"),
     )


class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_pan_no = models.CharField(max_length=200)
    # emp_age = models.IntegerField(default=18, validators=[MaxValueValidator(100), MinValueValidator(1)])
    emp_age = models.IntegerField(max_length=254)
    emp_gender = models.CharField(max_length=200, choices=Gender)
    emp_email = models.CharField(max_length=254)
    emp_city = models.CharField(max_length=200, choices=City)

    def clean(self):
        for field in self._meta.fields:
            if isinstance(field, (models.CharField, models.TextField)):
                setattr(self, field.name, getattr(self, field.name).strip())

    def __str__(self):
        return self.emp_name
