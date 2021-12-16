from rest_framework import generics, permissions
from datetime import datetime

from izzi.models import User
from izzi.serializers import UserSerializer


class UsersListApiView(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = User.objects.all()
        date_of_registration = self.request.query_params.get('date_of_registration')
        if date_of_registration:
            queryset = User.objects.filter(date_of_registration=datetime.strptime(date_of_registration, '%Y/%m/%d'))
        return queryset
