from django.contrib import admin
from .models import Farmer, Crop, Weather, MarketPrice, ChatbotConversation

# Register all models to appear in Django admin
admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(Weather)
admin.site.register(MarketPrice)
admin.site.register(ChatbotConversation)
