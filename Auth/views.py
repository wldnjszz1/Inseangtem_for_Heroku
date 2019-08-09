from rest_framework import generics
from .serializers import IstUserSerializer
from .models import IstUser

class IstUserListView(generics.ListAPIView):
    queryset = IstUser.objects.all()
    serializer_class = IstUserSerializer