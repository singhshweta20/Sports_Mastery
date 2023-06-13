from django.contrib import admin
# Register your models here.
from .models import Event,Contact,Feedback_Rating,Employee,Sport ,Sport_Plan,Tip,Student,User_Message,Student_Feedback,Coach_Assign


class Event_Admin(admin.ModelAdmin):
    list_display=('event_name','event_description','event_venue','event_date')
    search_fields=('event_date',)
    list_filter=['event_date']
    
class Event_Contact(admin.ModelAdmin):
    list_display=('name','email','phone','user_query','date')

class Student_Admin(admin.ModelAdmin):
    list_display=('student_id','student_name','student_email','student_phone',)
    
class Employee_Admin(admin.ModelAdmin):
    list_display=('employee_id','employee_name','email','phone','type')
    
admin.site.register(Event,Event_Admin)
admin.site.register(Contact,Event_Contact)
admin.site.register(Feedback_Rating)
admin.site.register(User_Message)
admin.site.register(Employee,Employee_Admin)
admin.site.register(Sport)
admin.site.register(Sport_Plan)
admin.site.register(Tip)
admin.site.register(Student,Student_Admin)
admin.site.register(Student_Feedback)
admin.site.register(Coach_Assign)

admin.site.site_header="Sports_Mastery_Administration"
admin.site.site_title="Admin Dashboard"
admin.site.index_title="Welcome to Student Mastery"