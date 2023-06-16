from django.db import models





# Agent Model

class Agent(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='houses',default="agent.png")
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):

        return self.name
    
    class Meta:

        ordering = ['name']


class House(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    house_type = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    beds = models.CharField(max_length=100)
    baths  = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='houses')
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Amenities(models.Model):
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


# Movers Model


class Mover(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    rate = models.DecimalField(max_digits=4, decimal_places=2)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rate']



class Facilities(models.Model):
    name = models.CharField(max_length=255)
    description =  models.CharField(max_length=500)
    image = models.ImageField(upload_to='houses',default="agent.png")
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']