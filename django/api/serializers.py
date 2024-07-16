from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
