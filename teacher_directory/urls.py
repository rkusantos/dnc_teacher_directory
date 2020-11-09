from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'teacher_directory'

urlpatterns = [
    #MKT Reports
    path('teacher_subject_list/', views.TeacherSubjectListView.as_view(template_name="teacher_directory/teacher_subject_list.html"), name='teacher_subject_list'),
]