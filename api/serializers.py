from rest_framework import serializers
from api import models

class DateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DateTime
        fields = "__all__"


class HistoryModelSerializer(serializers.ModelSerializer):

    dateTime = DateTimeSerializer(read_only=True, many=True)

    class Meta:
        model = models.HistoryModel
        fields = "__all__"

class UserModelSerializer(serializers.ModelSerializer):

    userDetail = HistoryModelSerializer()

    class Meta:
        model = models.UserModel
        fields = "__all__"