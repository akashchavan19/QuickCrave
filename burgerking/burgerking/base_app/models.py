from django.db import models

# Create your models here.

class ItemList(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class Items(models.Model):
    item_name = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    price=models.IntegerField()
    category=models.ForeignKey(ItemList, related_name='items',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.item_name

class AboutAs(models.Model):
    Description = models.TextField(blank=False)

class BookTable(models.Model):
    Name =models.CharField(max_length=20)
    phone_number = models.IntegerField()
    Email =models.EmailField()
    Total_members =models.IntegerField()
    booking_date = models.DateField()
    
    def __str__(self):
        return self.Name


