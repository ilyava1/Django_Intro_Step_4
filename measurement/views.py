from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, AllSensorsSerializer, MeasurementSerializer
from rest_framework.response import Response

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorView(APIView):
    def post(self, request):
        '''
        Функция создания нового сенсора
        '''
        new_sensor = request.data
        ser = SensorSerializer(data=new_sensor)
        if ser.is_valid():
            ser.save()
            return Response({'message': 'Sensor created'}, status=201)
        else:
            return Response({'message': ser.errors}, status=400)


    def patch(self, request):
        """
        Функия изменения существующего сенсора
        """
        edited_sensor = request.data
        ser = SensorSerializer(data=edited_sensor)
        if ser.is_valid():
            ser.save()
            return Response({'message': 'Sensor modified'}, status=201)
        else:
            return Response({'message': ser.errors}, status=400)


    def get(self, request, pk=0):
        """
        Функция получения информции о сенсоре/сенсорах.

        Если параметр pk не перадан, то по умолчанию его значение
        присваивается =0 и функция извлекает список всех сенсоров.
        Иначе функция возвращает данные сенсора, id которого =pk
        """
        if pk==0:
            sensors = Sensor.objects.all()
            ser = AllSensorsSerializer(sensors, many=True)
            return Response(ser.data)
        else:
            sensor = Sensor.objects.filter(id=pk)
            ser = SensorSerializer(sensor, many=True)
            return Response(ser.data)


class MeasurementView(APIView):
    def get(self, request):
        all_meas = Measurement.objects.all()
        ser = MeasurementSerializer(all_meas, many=True)
        return Response(ser.data)

    def post(self, request):
        new_meas = request.data
        ser = MeasurementSerializer(data=new_meas)
        if ser.is_valid():
            ser.save()
            return Response({'message': 'Measurement created'}, status=201)
        else:
            return Response({'message': ser.errors}, status=400)
