from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BusinessTrip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ])

    def __str__(self):
        return f'{self.employee.name} to {self.destination}'