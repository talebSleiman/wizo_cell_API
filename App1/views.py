from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     http_method_names = ['get']
#
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True,context={'request': request})
    return Response(data=serializer.data,status=status.HTTP_200_OK)