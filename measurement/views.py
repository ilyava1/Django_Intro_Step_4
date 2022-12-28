from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from rest_framework.response import Response

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# class SensorView(APIView):
#     def post(self, request):
#         new_sensor = request.data
#         ser = SensorSerializer(data=new_sensor)
#         if ser.is_valid():
#             ser.save()
#             print('ser.is_valid, ser.save')
#             return Response({'message': 'Sensor created'}, status=201)
#         else:
#             return Response({'message': ser.errors}, status=400)
#
#     def patch(self, request):
#         SensorSerializer(request.query_params)
#         return Response(f'Sensor updated')
#
#     def get(self, request, pk=0):
#         if pk==0:
#             sensors = Sensor.objects.all()
#             ser = SensorSerializer(sensors, many=True)
#         else:
#             sensor = Sensor.objects.filter(id=pk)
#             ser = SensorDetailSerializer(sensor, many=True)
#         return Response(ser.data)

#
# @api_view(['POST'])
# def add_measurement(request):
#     a_measurement = {
#         'name': 'name',
#         'messsge': 'Измерение добавлено'
#     }
#     return Response(a_measurement)



# class SensorView2(RetrieveAPIView):
#     queryset = Sensor.objects.all.measurements()
#     serializer_class = GetSensorSerializer

# @api_view(['POST'])
# def create_sensor(request):
#     create_sensor_dict = {}
#
#     create_sensor_dict = {
#         'name': 'name',
#         'description': 'description',
#         'messsge': 'Сенсор успешно создан'
#     }
#     return Response(create_sensor_dict)
#
#
# @api_view(['PATCH'])
# def edit_sensor(request):
#     edit_sensor_dict = {}
#
#     edit_sensor_dict = {
#         'name': 'name',
#         'description': 'description',
#         'messsge': 'Сенсор успешно изменен'
#     }
#     return Response(edit_sensor_dict)
#
#
# @api_view(['GET'])
# def get_sensor(request):
#
#     a_sensor = {
#         'name': 'name',
#         'description': 'description',
#         'messsge': 'Информация по датчику'
#     }
#     return Response(a_sensor)