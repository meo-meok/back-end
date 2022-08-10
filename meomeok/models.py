from django.db import models

# Mat-jip Database Model

class Users(models.Model) :
    user_id = models.IntegerField(default = 1)
    user_name = models.CharField(max_length = 5)
    authority = models.IntegerField(default = 0)

class Restaurant(models.Model) :
    restaurant_id = models.IntegerField(default = 1)
    restaurant_name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    category = models.IntegerField(default = 0)
    number = models.CharField(max_length = 14)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default = 0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default = 0.0)
    
class Review (models.Model) :
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    star = models.FloatField(default = 0.0)
    post_date = models.DateTimeField('date published')
    post_body = models.TextField()

class menu_price (models.Model) :
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    menu_name = models.CharField(max_length=20)
    menu_price = models.IntegerField()
