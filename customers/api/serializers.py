from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('fname', 'lname', 'email', 'mobile', 'myinfo')