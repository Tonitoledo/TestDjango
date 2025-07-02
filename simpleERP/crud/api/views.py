import logging

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from serializers import InvoiceSerializer
from crud.models import Invoice

logger = logging.getLogger(__name__)

class InvoiceViewSet(ViewSet):

    def list(self, request):
        serializer = InvoiceSerializer(Invoice.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self, request, pk=None):
        serializer = InvoiceSerializer(Invoice.objects.all(pk=pk))
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        serializer = InvoiceSerializer(Invoice.objects.all(pk=pk))
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            else:
                raise Exception
        except Exception as e:
            logger.exception("Error al crear la factura")


    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass