from django.contrib import admin
from app_price_prediction.models import car_data,review_data
# Register your models here.
admin.site.register(car_data)
admin.site.register(review_data)
