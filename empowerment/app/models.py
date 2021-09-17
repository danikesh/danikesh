from django.db import models

# Create your models here.
# Create your models here.
class Signup(models.Model):
    
     Email= models.EmailField()
     Passwd = models.CharField(max_length =30)


class Application(models.Model):
    
     name= models.CharField(max_length=50)
     email_address= models.EmailField(max_length=100)
     message= models.TextField (max_length = 30)

     def __str__(self):
        return str(self.name)
