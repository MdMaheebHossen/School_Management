from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE, null=True)

    def __str__(self):
        return f"{self.username}"

class BasicInfoModel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='profile_img/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class StudentModel(BasicInfoModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile', null=True, blank=True)
    roll_no = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class TeacherModel(BasicInfoModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    joining_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"