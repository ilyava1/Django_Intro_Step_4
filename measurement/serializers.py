from rest_framework import serializers
from .models import Sensor, Measurement


# Изменить датчик. Указываются название и/или описание.
# ЕСТЬ Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.

# Добавить измерение. Указываются ID датчика и температура.
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor_id', 'temperature', 'date']

# Создать датчик. Указываются название и описание датчика.
class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

# Получить информацию по конкретному датчику. Выдается полная информация по датчику:
# ID, название, описание и список всех измерений с температурой и временем.
# class SensorDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description']
