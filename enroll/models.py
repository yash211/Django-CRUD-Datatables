from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
#makemigrations-creates sql stat
#sqlmigrate=shows tables
#showmigration-shows all previous migration
#where->get

def pass_validation(password):
    if len(password)>4:
        raise ValidationError("Password is too long")


class Student(models.Model):
    # studid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.CharField(max_length=70)
    stupass=models.CharField(max_length=70,validators=[pass_validation])


