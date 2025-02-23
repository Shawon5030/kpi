from django.db import models
from django.contrib import admin

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ['name', 'short_name']
    ordering = ['name']

admin.site.register(Teacher, TeacherAdmin)

class Room(models.Model):
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f'Room {self.room_number}'

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number',)
    search_fields = ['room_number']
    ordering = ['room_number']

admin.site.register(Room, RoomAdmin)

class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.code} - {self.name}'

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ['code', 'name']
    ordering = ['code']

admin.site.register(Subject, SubjectAdmin)

class ClassSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    period = models.IntegerField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    group = models.CharField(max_length=20, default="A1+B1")

    def __str__(self):
        return f'{self.day} - Period {self.period} ({self.subject.code})'

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 'period', 'time_start', 'time_end', 'subject', 'teacher', 'room', 'group')
    search_fields = ['day', 'period', 'subject__code', 'teacher__name', 'room__room_number', 'group']
    ordering = ['day', 'period']

admin.site.register(ClassSchedule, ClassScheduleAdmin)
