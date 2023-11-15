from django.urls import path
from . import views


urlpatterns = [
    path("", views.category_list_view, name="category-list"),
    path("exercise/", views.exercise_list_view, name="exercise-list"),
    path("service/", views.service_list_view, name="service-list"),
    path("testimonial/", views.testimonial_list_view, name="testimonials-list")

]
