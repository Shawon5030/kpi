from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form-data', views.form_data, name='form_data'),
    path('api/teachers/', views.TeacherListCreate.as_view(), name='teacher-list-create'),
    path('api/teachers/<int:pk>/', views.TeacherRetrieveUpdateDestroy.as_view(), name='teacher-detail'),
    path('api/rooms/', views.RoomListCreate.as_view(), name='room-list-create'),
    path('api/rooms/<int:pk>/', views.RoomRetrieveUpdateDestroy.as_view(), name='room-detail'),
    path('api/subjects/', views.SubjectListCreate.as_view(), name='subject-list-create'),
    path('api/subjects/<int:pk>/', views.SubjectRetrieveUpdateDestroy.as_view(), name='subject-detail'),
    path('api/class-schedules/', views.ClassScheduleListCreate.as_view(), name='class-schedule-list-create'),
    path('api/class-schedules/<int:pk>/', views.ClassScheduleRetrieveUpdateDestroy.as_view(), name='class-schedule-detail'),
]
