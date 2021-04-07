from django.shortcuts import render,HttpResponse,render
from django.contrib import messages
from app_price_prediction.models import car_data,review_data

import pickle
# python manage.py runserver
model=pickle.load(open("gradient_boosting_Regressor.pkl",'rb'))
# from SGDClassifier.pkl import cleaned_data
review_model=pickle.load(open("SGDClassifier.pkl",'rb'))
# from SGDClassifier import cleaned_data
# Create your views here.
def home(request):
    if request.method=="POST":

        original_price=request.POST.get("originalPrice")
        original_price=float(original_price)/100000
        
        kms_driven=request.POST.get("kmsDriven")

        fuel_type=request.POST.get("fuel")
        Fuel_Type_Diesel=0
        Fuel_Type_Petrol=1
        if(fuel_type=="petrol"):
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=1
        elif(fuel_type=="diesel"):
            Fuel_Type_Diesel=1
            Fuel_Type_Petrol=0
        elif(fuel_type=="CNG"):
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=0

        seller_type=request.POST.get("seller")
        Seller_Type_Individual=0
        if(seller_type=="individual"):
            Seller_Type_Individual=1
        
        car_brand=request.POST.get("brand")
        

        from datetime import date 
        current_year = date.today().year
        
        registration_year=request.POST.get("year")
        age_vehicle=current_year-int(registration_year)

        transmission_type=request.POST.get("transmission")
        Transmission_Manual=0
        if(transmission_type=="manual"):
            Transmission_Manual=1
         
        past_owners=request.POST.get("owners")
        past_owners=int(past_owners)

        ans=model.predict([[original_price,float(kms_driven),past_owners,age_vehicle,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        price=int(ans*100000)
        
        if(ans>original_price):
            messages.warning(request,"Sorry...Price Of Car is Too Less. We are Working for These Cars")
        elif(ans):
          carData=car_data(originalPrice=int(original_price*100000) ,kmsDriven=int(kms_driven) ,brandName=car_brand,fuelType=fuel_type,pastOwners=past_owners,transmissionType=transmission_type,registrationYear=registration_year,sellerType=seller_type,sellingPrice=price)
          carData.save()
          messages.success(request,"Price Of This Car Is Rs. "+ str(price))
    return render(request,"index.html")

def feedback(request):
    if request.method=="POST":
        review=request.POST.get("review")
        sentiment=review_model.predict([review])
        if(sentiment[0]==0):
          sentiment="negative review"
          messages.info(request,"Thanks for your review. We will improve")
          reviewData=review_data(review=review,sentiment=sentiment)
          reviewData.save()
        else:
          sentiment="positive review"
          messages.success(request,"Thanks for your review. Happy to see your positive review")
          reviewData=review_data(review=review,sentiment=sentiment)
          reviewData.save()
        return render(request,"feedback.html")
 
    return render(request,"feedback.html")
