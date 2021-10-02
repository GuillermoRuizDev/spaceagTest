from rest_framework import serializers
from .models import FieldWorker

class FieldWorkerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldWorker
        fields = ('first_name', 'last_name', 'function')
