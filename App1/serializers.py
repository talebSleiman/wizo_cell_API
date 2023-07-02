from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # def get_image(self, obj):
    #     request = self.context.get('request')
    #     if obj.image:
    #         return request.build_absolute_uri(obj.image.url)
    #     return None
    class Meta:
        model = Product
        fields = '__all__'