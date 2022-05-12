from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializers):
    class Meta:
        model  = Drink