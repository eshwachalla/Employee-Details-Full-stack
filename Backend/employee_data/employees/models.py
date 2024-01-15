from django.db import models

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_address = models.CharField(max_length=200)
    emp_salary = models.DecimalField(max_digits=10, decimal_places=2)
    emp_designation = models.CharField(max_length=50)
