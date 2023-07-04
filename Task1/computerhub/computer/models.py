from django.db import models

# Create your models here.
class ComputerBrands(models.Model):
    brand_name=models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/',default="")
    def __str__(self):
        return self.brand_name
    
class ComputerSpecification(models.Model):
    generation = models.IntegerField()    
    price_min = models.FloatField()
    price_max = models.FloatField()
    ram=models.IntegerField()
    brand = models.ForeignKey(ComputerBrands, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.generation} - {self.brand}"
class Computer(models.Model):
    computer_code=models.CharField(max_length=100, unique=True)
    specification=models.ForeignKey(ComputerSpecification, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    unit_rate=models.IntegerField()
    total_price=models.IntegerField()
    def save(self,*args,**kwargs):
        self.total_price=self.quantity*self.unit_rate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.computer_code

    