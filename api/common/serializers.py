from rest_framework import serializers


class MetadataSerializer(serializers.Serializer):
    class Meta:
        fields = ["created_at", "updated_at"]
