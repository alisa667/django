from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.template.response import TemplateResponse

from hello import forms, models

def start(request):
    return TemplateResponse(request, 'start.html')

def university_list(request):
    universities = models.University.objects.all()
    data = {'universities': universities}
    return TemplateResponse(request, 'university_list.html', data)

def student_list(request):
    all_studs = models.Student.objects.all()
    data = {'students': all_studs}
    return TemplateResponse(request, 'student_list.html', data)

def create_university(request):
    form = forms.UniversityForm()

    if request.method == 'POST':
        form = forms.UniversityForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            models.University(full_name=cd['full_name'],
                              short_name=cd['short_name'],
                              creation_date=cd['creation_date']).save()

            return HttpResponseRedirect('/hello/universities/')
        else: 
            return HttpResponseNotFound("Invalid data format")
    else:
        data = {'form': form}
        return render(request, 'university.html', data)

def create_student(request):
    form = forms.StudentForm()

    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            models.Student(name=cd['name'],
                           date_of_birth=cd['date_of_birth'],
                           university=cd['university'],
                           admission_year=cd['admission_year']).save()

            return HttpResponseRedirect('/hello/students/')
        else: 
            return HttpResponseNotFound("Invalid data format")

    else:
        data = {'form': form}
        return render(request, 'student.html', data)


def delete_university(request, uni_id):
    try:
        university = models.University.objects.get(id=uni_id)
        university.delete()
        return HttpResponseRedirect('/hello/universities/')
    except models.University.DoesNotExist:
        return HttpResponseNotFound("University with this id not found")

def delete_student(request, s_id):
    try:
        student = models.Student.objects.get(id=s_id)
        student.delete()
        return HttpResponseRedirect("/hello/students/")
    except models.Student.DoesNotExist:
        return HttpResponseNotFound("Student with this id not found")


def update_university(request, uni_id):
    university = models.University.objects.get(id=uni_id)
    form = forms.UniversityForm(instance=university)

    if request.method == 'POST':
        form = forms.UniversityForm(request.POST, instance=university)
        if form.is_valid():
            cd = form.cleaned_data
            models.University.objects.filter(id=uni_id).update(full_name=cd['full_name'],
                                                                  short_name=cd['short_name'],
                                                                  creation_date=cd['creation_date'])
            return HttpResponseRedirect('/hello/universities/')
        else: 
            return HttpResponseNotFound("Invalid data format")
    else:
        data = {'form': form}
        return render(request, 'university.html', data)


def update_student(request, s_id):
    student = models.Student.objects.get(id=s_id)
    form = forms.StudentForm(instance=student)

    if request.method == 'POST':
        form = forms.StudentForm(request.POST, instance=student)
        if form.is_valid():
            cd = form.cleaned_data
            models.Student.objects.filter(id=s_id).update(name=cd['name'],
                                                             date_of_birth=cd['date_of_birth'],
                                                             university=cd['university'],
                                                             admission_year=cd['admission_year'])
            return HttpResponseRedirect('/hello/students/')
        else: 
            return HttpResponseNotFound("Invalid data format")

    else:
        data = {'form': form}
        return render(request, 'student.html', data)
