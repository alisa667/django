from django.db import models

class University(models.Model):
    full_name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=20)
    creation_date = models.DateField()

    def __str__(self):
        return f'{self.full_name}'

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    admission_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}_{self.university}'
