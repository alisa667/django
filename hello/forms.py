from django import forms
from hello.models import University, Student

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['full_name', 'short_name', 'creation_date']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'university', 'admission_year']


