from rest_framework import serializers
from .models import user_data


class DataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_data
        fields = ['wallet_address', 'twitter_link']
        read_only_fields = ['id']
