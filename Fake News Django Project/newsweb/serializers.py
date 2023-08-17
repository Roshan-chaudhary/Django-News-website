# import serializer from rest_framework
from rest_framework import serializers
from .models import Image
 
# Create a model serializer
class ImageSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Image
        fields = '__all__'