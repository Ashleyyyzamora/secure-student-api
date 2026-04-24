from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from student_records.views import StudentRecordViewSet

router = DefaultRouter()
router.register(r'student-records', StudentRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    
    path('api/', include(router.urls)),
]