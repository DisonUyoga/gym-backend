from django.contrib import admin
from .models import Pricing,Service, ExerciseBenefit, Class_Category, Booked_Class, Testimonial

admin.site.register(ExerciseBenefit)
admin.site.register(Class_Category)
admin.site.register(Booked_Class)
admin.site.register(Pricing)
admin.site.register(Service)
admin.site.register(Testimonial)