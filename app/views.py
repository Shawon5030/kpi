from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from .models import ClassSchedule, Teacher, Room, Subject
import datetime
from rest_framework import generics
from .serializers import TeacherSerializer, RoomSerializer, SubjectSerializer, ClassScheduleSerializer

# Create your views here.
def home(request):
    # ...existing code...
    return render(request, 'home.html')

def form_data(request):
    data = request.GET['name']
    print(data)
    data_list = [i.lower() for i in data.split(' ')]
    
    current_date = datetime.datetime.now()
    day_name = current_date.strftime("%A")
    tomorrow_date = current_date + datetime.timedelta(days=1)
    tomorrow_day_name = tomorrow_date.strftime("%A")
   
    if 'today' in data_list and 'first' in data_list and 'class' in data_list:
        return_data = ClassSchedule.objects.filter(day=day_name).order_by('period').first()
        data = {
            'classes': [
                {
                    'day': return_data.day,
                    'period': return_data.period,
                    'start_time': return_data.time_start,
                    'end_time': return_data.time_end,
                    'subject': return_data.subject.name,
                    'teacher': return_data.teacher.name,
                    'room': return_data.room.room_number if return_data.room else None,
                    'group': return_data.group
                }
            ]
        }
        return JsonResponse(data)
    
    elif 'today' in data_list and 'total' in data_list and 'class' in data_list:
        return_data = ClassSchedule.objects.filter(day=day_name)
        data = {
            'total_classes': return_data.count()
        }
        return JsonResponse(data)
    
    elif 'sir' in data_list and 'time' in data_list:
        teacher_name = data_list[data_list.index('sir') + 1]
        teacher = Teacher.objects.filter(name__icontains=teacher_name).first()
        if teacher:
            return_data = ClassSchedule.objects.filter(teacher=teacher, day=day_name)
            data = {
                'classes': [
                    {
                        'day': item.day,
                        'period': item.period,
                        'start_time': item.time_start,
                        'end_time': item.time_end,
                        'subject': item.subject.name,
                        'teacher': item.teacher.name,
                        'room': item.room.room_number if item.room else None,
                        'group': item.group
                    } for item in return_data
                ]
            }
            return JsonResponse(data)
    
    elif 'tomorrow' in data_list:
        return_data = ClassSchedule.objects.filter(day=tomorrow_day_name)
        data = {
            'classes': [
                {
                    'day': item.day,
                    'period': item.period,
                    'start_time': item.time_start,
                    'end_time': item.time_end,
                    'subject': item.subject.name,
                    'teacher': item.teacher.name,
                    'room': item.room.room_number if item.room else None,
                    'group': item.group
                } for item in return_data
            ]
        }
        return JsonResponse(data)
    
    elif 'today' in data_list:
        return_data = ClassSchedule.objects.filter(day=day_name)
        data = {
            'classes': [
                {
                    'day': item.day,
                    'period': item.period,
                    'start_time': item.time_start,
                    'end_time': item.time_end,
                    'subject': item.subject.name,
                    'teacher': item.teacher.name,
                    'room': item.room.room_number if item.room else None,
                    'group': item.group
                } for item in return_data
            ]
        }
        return JsonResponse(data)
    
    elif 'sir' in data_list:
        input_sir_name = data_list[1]
        return_data = ClassSchedule.objects.filter(teacher__name__icontains=input_sir_name)
        data = {
            'classes': [
                {
                    'day': item.day,
                    'period': item.period,
                    'start_time': item.time_start,
                    'end_time': item.time_end,
                    'subject': item.subject.name,
                    'teacher': item.teacher.name,
                    'room': item.room.room_number if item.room else None,
                    'group': item.group
                } for item in return_data
            ]
        }
        return JsonResponse(data)
    
    elif 'day' in data_list:
        if data_list[1] == 'sun':
            return_data = ClassSchedule.objects.filter(day='Sunday')
        elif data_list[1] == 'mon':
            return_data = ClassSchedule.objects.filter(day='Monday')    
        elif data_list[1] == 'tue':
            return_data = ClassSchedule.objects.filter(day='Tuesday')
        elif data_list[1] == 'wed':
            return_data = ClassSchedule.objects.filter(day='Wednesday')
        elif data_list[1] == 'thu':
            return_data = ClassSchedule.objects.filter(day='Thursday')
        elif data_list[1] == 'fri':
            return_data = ClassSchedule.objects.filter(day='Friday')
        elif data_list[1] == 'sat':
            return_data = ClassSchedule.objects.filter(day='Saturday')
       
        data = {
            'classes': [
                {
                    'day': item.day,
                    'period': item.period,
                    'start_time': item.time_start,
                    'end_time': item.time_end,
                    'subject': item.subject.name,
                    'teacher': item.teacher.name,
                    'room': item.room.room_number if item.room else None,
                    'group': item.group
                } for item in return_data
            ]
        }
        return JsonResponse(data)
    
    else:
        return JsonResponse({'message': 'ক্ষম করুন, আমি বুঝতে পারছি না'}, status=400)

class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class SubjectListCreate(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ClassScheduleListCreate(generics.ListCreateAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer

class ClassScheduleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassSchedule.objects.all()
    serializer_class = ClassScheduleSerializer