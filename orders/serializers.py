from .models import Order
from rest_framework import serializers



class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default= 'PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order 
        fields = ['id','order_status', 'size', 'quantity']
        
class OrderDetailSerializer(serializers.ModelSerializer):
    
    order_status = serializers.CharField(default= "PENDING")
    size = serializers.CharField(max_length=20)
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Order 
        fields=['id','order_status', 'size', 'quantity', 'created_at', 'updated_at'] 

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default="PENDING")

    class Meta:
        model = Order 
        fields=['order_status']
