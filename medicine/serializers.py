from rest_framework import serializers
from .models import Medicine


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = (
            'code',
            'name',
            'description',
            'medicine_type',
            'amount',
        )


