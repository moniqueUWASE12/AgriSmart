# models.py
from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    registered_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Crop(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop_type = models.CharField(max_length=50)
    planting_date = models.DateField()
    harvest_date = models.DateField()

    def __str__(self):
        return f"{self.crop_name} ({self.farmer.name})"

class Weather(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.FloatField()
    rainfall = models.FloatField()

    def __str__(self):
        return f"Weather in {self.location} on {self.date}"

class MarketPrice(models.Model):
    crop_type = models.CharField(max_length=50)
    market_location = models.CharField(max_length=100)
    price_per_kg = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.crop_type} @ {self.price_per_kg} RWF ({self.market_location})"

class ChatbotConversation(models.Model):
    user_question = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Q: {self.user_question[:30]}... | {self.farmer.name}"
