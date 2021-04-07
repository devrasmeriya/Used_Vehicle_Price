from django.db import models

# Create your models here.
class car_data(models.Model):
     
     originalPrice=models.CharField(max_length=20,default="0")
     kmsDriven=models.CharField(max_length=20,default="0")
     brandName=models.CharField(max_length=20,default="0")
     fuelType=models.CharField(max_length=20,default="0")
     pastOwners=models.CharField(max_length=20,default="0")
     transmissionType=models.CharField(max_length=20,default="0")
     registrationYear=models.CharField(max_length=20,default="0")
     sellerType=models.CharField(max_length=20,default="0")
     sellingPrice=models.CharField(max_length=20,default="0")

     
     
     def __str__(self):
        return self.brandName,self.kmsDriven,self.originalPrice

class review_data(models.Model):
   review=models.CharField(max_length=200,default="null")
   sentiment=models.CharField(max_length=20,default="0")
   def __str__(self):
      return self.sentiment


  
