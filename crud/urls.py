from django.contrib import admin
from django.urls import path
from students.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudnetView.as_view(),name="home"),
    path('insert/', StudentFormView.as_view(),name="insert"),
    path('<pk>/edit-student/', EditStudentView.as_view(),name="EditStudentView"),
    path('<pk>/delete-student/', DeleteStudentView.as_view(),name="DeleteStudentView"),
]
