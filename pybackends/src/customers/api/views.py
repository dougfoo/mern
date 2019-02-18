from customers.models import Customer
from .serializers import CustomerSerializer

from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


# class UserListView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetailView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserCreateView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDeleteView(DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserUpdateView(UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
