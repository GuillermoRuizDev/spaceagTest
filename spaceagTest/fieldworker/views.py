#from django.shortcuts import render
from rest_framework import status, generics, mixins
from .models import FieldWorker
from .serializers import FieldWorkerModelSerializer
# Create your views here.
class FieldworkerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FieldworkerDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
