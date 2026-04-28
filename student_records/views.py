from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated
)

from django.http import JsonResponse

from .models import StudentRecord
from .serializers import StudentRecordSerializer
from .permissions import IsAdminOrFaculty

from cryptography.fernet import Fernet
from django_ratelimit.decorators import ratelimit

import logging


logger = logging.getLogger(__name__)

logger.warning(
    "Multiple failed login attempts detected"
)



key = Fernet.generate_key()
cipher = Fernet(key)

encrypted_data = cipher.encrypt(
    b"4111-1111-1111-1111"
)

print(encrypted_data)


@ratelimit(key='ip', rate='5/m')
def login_view(request):

    return JsonResponse({
        "message": "Login allowed"
    })


class StudentRecordViewSet(ModelViewSet):

    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer

    def get_permissions(self):

        if self.action in ['create', 'destroy']:

            permission_classes = [IsAdminUser]

        elif self.action in ['update', 'partial_update']:

            permission_classes = [IsAdminOrFaculty]

        else:

            permission_classes = [IsAuthenticated]

        return [
            permission()
            for permission in permission_classes
        ]