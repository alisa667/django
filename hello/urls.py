from django.urls import path
from . import views


urlpatterns = [
    path('', views.start, name="start"),
    
    path('students/', views.student_list),
    path('students/create/', views.create_student),
    path('students/update/<int:s_id>/', views.update_student),
    path('students/delete/<int:s_id>/', views.delete_student),

    path('universities/', views.university_list),
    path('universities/create/', views.create_university),
    path('universities/update/<int:uni_id>/', views.update_university),
    path('universities/delete/<int:uni_id>/', views.delete_university),

]