from rest_framework import serializers


class DealsGetSerializer(serializers.Serializer):
    response = serializers.ListField()


class DealsFileUploadSerializer(serializers.Serializer):
    deals = serializers.FileField()

    def validate_deals(self, file):
        if not file:
            raise serializers.ValidationError("Файл отсутствует")

        if not file.name.endswith('.csv'):
            raise serializers.ValidationError("Неверный формат файла")

        return file
