from rest_framework import generics
from .models import Class_Category, ExerciseBenefit, Service
from .serializers import TestimonialSerializer, CategorySerializer, ExerciseBenefitSerializer, ServiceSerializer, Testimonial


class ListAPIView(generics.ListAPIView):
  queryset=Class_Category.objects.all()
  serializer_class=CategorySerializer
category_list_view=ListAPIView.as_view()

class ListExerciseAPIView(generics.ListAPIView):
  queryset=ExerciseBenefit.objects.all()
  serializer_class=ExerciseBenefitSerializer
exercise_list_view=ListExerciseAPIView.as_view()

class ListServiceAPIView(generics.ListAPIView):
  queryset=Service.objects.all()
  serializer_class=ServiceSerializer
service_list_view=ListServiceAPIView.as_view()

class ListTestmonialAPIView(generics.ListAPIView):
  queryset=Testimonial.objects.all()
  serializer_class=TestimonialSerializer
testimonial_list_view=ListTestmonialAPIView.as_view()


