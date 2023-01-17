from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Plate
from .serializers import PlateSerializer


class PlateGenerateView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['get'])
    def generate(self, request):
        amount = request.query_params.get('amount', 1)
        try:
            amount = int(amount)
        except ValueError:
            amount = 1

        plates = Plate.generate_plate(amount)
        serializer = PlateSerializer(plates, many=True)
        return Response({"plates": serializer.data})


class PlateGetView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['get'])
    def get(self, request):
        plate_id = request.query_params.get('id', None)
        if plate_id is None:
            return Response({"error": "id is missing."}, status=400)
        try:
            plate = Plate.objects.get(id=plate_id)
            serializer = PlateSerializer(plate)
            return Response({"plate": serializer.data})
        except Plate.DoesNotExist:
            return Response({"error": "Plate not found."}, status=404)


class PlateAddView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['post'])
    def add(self, request):
        plate = request.data.get('plate')

        if not plate:
            return Response({"error": "plate is missing."}, status=400)
        if not Plate.is_valid_plate(plate):
            return Response({"error": "Invalid plate number."}, status=400)

        plate_obj = Plate.objects.create(plate_number=plate)
        return Response({"id": plate_obj.id})
