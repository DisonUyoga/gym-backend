from rest_framework import serializers
from .models import Class_Category, ExerciseBenefit, Pricing, Service, Testimonial


class ExerciseBenefitSerializer(serializers.ModelSerializer):
  class Meta:
    model=ExerciseBenefit
    fields=[
      "id",
      "title",
      "imgUrl",
      "benefit",
    ]

class CategorySerializer(serializers.ModelSerializer):
  
  class Meta:
    model=Class_Category
    fields=(
      "id",
      "date",
      "type_of_exercise",
      "available",
      "center",
      "pricing",
      "start_time",
      "stop_time",
      "book",
     
    )

class PricingSerializer(serializers.Serializer):
  
  class Meta:
    model=Pricing
    field=(
      "id",
      "member_type",
      "price",
      "period"
    )
 
 
class ServiceSerializer(serializers.ModelSerializer):

  member=serializers.SerializerMethodField(read_only=True)
  price=serializers.SerializerMethodField(read_only=True)
  period=serializers.SerializerMethodField(read_only=True)
  class Meta:
    model=Service
    fields=(
      "id",
      "service_item",
      "member",
      "member_type",
      "price",
      "period",
    )
  def get_member(self, obj):
    return obj.member_type.member_type
  def get_price(self, obj):
    return obj.member_type.price
  def get_period(self, obj):
    return obj.member_type.period

class TestimonialSerializer(serializers.ModelSerializer):
  class Meta:
    model=Testimonial
    fields=(
      "id",
      "name",
      "imgUrl",
      "description",
    )
  

