from rest_framework import generics, status
from rest_framework.response import Response
from django.core.cache import cache


from .models import Deal
from .serializers import DealsFileUploadSerializer, DealsGetSerializer
from .utils import object_for_response, parse_csv


class DealsGet(generics.RetrieveAPIView):
    serializer_class = DealsGetSerializer

    def get_object(self):
        queryset = cache.get_or_set('deals', Deal.objects.all())
        obj = object_for_response(queryset)

        return obj


class DealsCreate(generics.CreateAPIView):
    serializer_class = DealsFileUploadSerializer

    def post(self, request, *args, **kwargs):
        existing_deals = Deal.objects.all()
        if existing_deals:
            existing_deals.delete()
            cache.delete('deals')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        deals = serializer.validated_data['deals']
        deals_list = parse_csv(deals)
        deals_objects = Deal.objects.bulk_create(deals_list)

        if deals_objects:
            return Response(
                data={
                    'Status': 'OK - файл был обработан без ошибок'
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data={
                    'Status': 'Error',
                    'Desc': 'в процессе обработки файла произошла ошибка'
                },
                status=status.HTTP_400_BAD_REQUEST,
                exception=True,
            )
