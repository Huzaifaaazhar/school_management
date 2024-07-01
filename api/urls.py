from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassViewSet, CourseViewSet, StudentViewSet, StudentCoursesView, MarkViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'marks', MarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('students/<int:pk>/courses/', StudentCoursesView.as_view(), name='student-courses'),
]