from rest_framework import generics
from .models import Drf
from .serializers import DrfSerializer
from .permissions import IsOwnerOrReadOnly


class DrfList(generics.ListCreateAPIView):
    queryset = Drf.objects.all()
    serializer_class = DrfSerializer


class DrfDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Drf.objects.all()
    serializer_class = DrfSerializer
