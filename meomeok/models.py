from django.db import models

# Create your models here.

class Users(models.Model) :
    user_id = models.IntegerField(default = 1)
    user_name = models.CharField(max_length = 5)
    authority = models.IntegerField(default = 0)

class Restarunt(models.Model) :
    rest_id = models.IntegerField(default = 1)
    rest_name = models.CharField(max_length = 30)
    rest_number = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    category = models.IntegerField(default = 0)
    number = models.CharField(max_length = 14)
    
class Review (models.Model) :
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rest = models.ForeignKey(Restarunt, on_delete=models.CASCADE)
    rest_star = models.FloatField(default = 0.0)
    post_date = models.DateTimeField('date published')
    post_body = models.TextField()

class menu_price (models.Model) :
    rest = models.ForeignKey(Restarunt, on_delete = models.CASCADE)
    menu_name = models.CharField(max_length=20)
    menu_price = models.IntegerField()

class rest_location (models.Model) :
    rest = models.ForeignKey(Restarunt, on_delete = models.CASCADE)
    x_axis = models.DecimalField(max_digits=9, decimal_places=6)
    y_axis = models.DecimalField(max_digits=9, decimal_places=6)
