from django.contrib import admin
from users_auth.models import CustomUser, BasicInfoModel, StudentModel, TeacherModel


admin.site.register(CustomUser)
admin.site.register(BasicInfoModel)
admin.site.register(StudentModel)