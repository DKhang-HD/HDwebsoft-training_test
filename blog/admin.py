from django.contrib import admin
from .models import Question, Choice
# user: Khang_admin
# pass: Khang_admin

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)