from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Check
from .serializers import CheckSerializer
# from django_filters.rest_framework import DjangoFilterBackend

class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    permission_classes = [AllowAny]  # No login required
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payer_name', 'date_received', 'amount']

    # No need for user-based filtering
    def get_queryset(self):
        return self.queryset

    # No user linking on create
    def perform_create(self, serializer):
        serializer.save()
