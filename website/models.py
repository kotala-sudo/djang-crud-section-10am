from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return (f'{self.first_name} {self.last_name}')
