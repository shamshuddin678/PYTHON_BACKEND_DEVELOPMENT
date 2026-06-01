from django.db import models

'''
->makemigrations = create changes and store them ina file
->migrations = apply the pending changes created by makemigrations
'''

# Create your models here.
# creating the table
class Contact(models.Model):
    name = models.CharField( max_length=122) 
    email = models.CharField( max_length=122)
    Phone  = models.CharField( max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name