"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("login_validate/", views.loginValidate),
    path("user_login_validate/", views.userLoginValidate),
    path("admin/", views.adminAdmin),
    path("days/", views.days),
    path("notifications/", views.notifications),
    path("report/", views.report),
    path("report_details/", views.report_details),
    path("notifications_details/", views.send_notifications),
    path("subject/", views.subject),
    path("faculty/", views.faculty),
    path("students/", views.students),
    path("class/", views.classes),
    path("attendance/", views.attendance),
    path("admin_login/", views.adminLogin),
    path("admin_details/", views.adminDetails),
    path("days_details/", views.days_details),
    path("subject_details/", views.subject_details),
    path("faculty_details/", views.faculty_details),
    path("student_details/", views.student_details),
    path("class_details/", views.class_details),
    path("attendance_details/", views.attendance_details),
    path("check_user_session/", views.checkUserSession),
    path("web_logout/", views.webLogout),
    path("logout/", views.Logout),
    path("", views.camera),
    path("train_model/", views.trainModel),
    path("class_attendance/", views.classAttendance),
]
