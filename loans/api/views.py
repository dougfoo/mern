from loans.models import Loan
from .serializers import LoanSerializer

from rest_framework import viewsets


class LoanViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()


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
