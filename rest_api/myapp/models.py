from django.db import models

# Create your models here.
class Employee(models.Model):

   first_name = models.CharField(max_length = 50)
   last_name = models.CharField(max_length = 50)
   age = models.IntegerField()
   company_name = models.CharField(max_length = 80)
   city = models.CharField(max_length = 50)
   state = models.CharField(max_length = 50)
   zip_code = models.CharField(max_length = 50)
   email = models.EmailField()
   web = models.CharField(max_length = 100)
   
   def __str__(self):
       return self.first_name

   class Meta:
      db_table = "employee"

    