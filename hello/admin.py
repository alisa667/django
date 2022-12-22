from django.contrib import admin
from .models import Student, University

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'short_name', 'creation_date')

admin.site.register(University, UniversityAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'university', 'admission_year')

admin.site.register(Student, StudentAdmin)


