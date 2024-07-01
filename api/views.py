from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, generics
from .models import Teacher, Class, Course, Student, Mark
from .serializers import TeacherSerializer, ClassSerializer, CourseSerializer, StudentSerializer, MarkSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']

    @action(detail=True, methods=['get'])
    def courses(self, request, pk=None):
        student = self.get_object()
        courses = Course.objects.filter(marks__student=student)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class StudentCoursesView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        student_id = self.kwargs['pk']
        student = Student.objects.get(pk=student_id)
        return Course.objects.filter(students=student)

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['student__name', 'course__name', 'teacher__name']
