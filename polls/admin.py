from django.contrib import admin
from .models import Choice
from .models import Question
from .models import Company
from .models import Employee
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Company)
admin.site.register(Employee)