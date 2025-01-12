from django.contrib import admin
from django.urls import path
from mywebsite import views

urlpatterns = [
    path('myadmin/', admin.site.urls),  # Admin URL
    path('student-grades/', views.studentGrades, name='student-grades'),  # Grades page
    path('', views.studentGrades, name='home'),  # Root URL
]
