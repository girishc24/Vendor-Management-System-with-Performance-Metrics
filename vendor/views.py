from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . models import Vendor, PurchaseOrder
from . serializers import VendorSerializer, PurchaseOrderSerializer

def main(request):
    return HttpResponse("Hello world!")


class VendorDetails(APIView):
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #validated_data = serializer.validated_data
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        queryset = Vendor.objects.all()
        serializer =VendorSerializer(queryset, many=True)
        return Response(serializer.data)




@api_view(['GET', 'PUT', 'DELETE'])
def vendordetails(request, pk):
    if request.method == 'GET':
        queryset = Vendor.objects.filter(id=pk)
        vedor_serializer = VendorSerializer(queryset, many=True)
        return Response(vedor_serializer.data)
    
    elif request.method == 'PUT':
        vendor_instance = Vendor.objects.get(id=pk)
        serializer = VendorSerializer(vendor_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        vendor_instance= Vendor.objects.filter(id=pk).first()
        if vendor_instance:
            vendor_instance.delete()
            return Response({"message": "Vendor deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)




class PurchaseOrderDeatils(APIView):

    def post(self, request):
        serializer=PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        queryset = PurchaseOrder.objects.all()
        seralizer = PurchaseOrderSerializer(queryset, many=True)
        return Response(seralizer.data, status=status.HTTP_200_OK)