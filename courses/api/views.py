from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer


from rest_framework.response import Response
from ..models import Course

from rest_framework import viewsets
from .serializers import CourseSerializer



class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)