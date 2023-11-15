from django.db import models
from django.conf import settings


User=settings.AUTH_USER_MODEL
class ExerciseBenefit(models.Model):
  title=models.CharField(max_length=255)
  imgUrl=models.ImageField(upload_to="media")
  benefit=models.TextField()
  
  def __str__(self):
    return f"{self.title}"
  


class Pricing(models.Model):
  member_type=models.CharField(max_length=255)
  price=models.DecimalField(max_digits=15, decimal_places=2)
  period=models.CharField(max_length=255, blank=True,null=True)

  def __str__(self):
    return f"Service: {self.member_type} ----- Price: {self.price}"

class Service(models.Model):
  service_item=models.CharField(max_length=255)
  member_type=models.ForeignKey(Pricing, on_delete=models.CASCADE, default="")

  def __str__(self):
    return f"Service: {self.service_item}---- {self.member_type}"



class Class_Category(models.Model):
  date=models.DateField(default=0)
  type_of_exercise=models.CharField(max_length=255)
  available=models.BooleanField(default=False)
  center=models.CharField(max_length=100)
  pricing=models.ForeignKey(Pricing, related_name="pricing", on_delete=models.CASCADE, blank=True, null=True)
  start_time=models.TimeField(default=0)
  stop_time=models.TimeField(default=0)
  book=models.BooleanField(default=False)

  class Meta:
    verbose_name="Class"
    verbose_name_plural="Classes"

  def __str__(self):
    return f"Exercise: {self.type_of_exercise} ---- Center: {self.center} ------ start: {self.start_time} - stop: {self.stop_time}"

class Booked_Class(models.Model):
  user=models.ForeignKey(User,default=1, on_delete=models.CASCADE)
  class_category=models.ForeignKey(Class_Category, on_delete=models.CASCADE)

  class Meta:
    verbose_name="Booked Class"
    verbose_name_plural="Booked Classes"

  def __str__(self):
    return f"Client: {self.user} ------  Booking: {self.class_category}"

class Testimonial(models.Model):
  name=models.CharField(max_length=255)
  imgUrl=models.ImageField(upload_to="media/")
  description=models.TextField()

  def __str__(self):
    return f"Name: {self.name}"


