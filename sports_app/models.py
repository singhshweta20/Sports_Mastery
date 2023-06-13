from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=50,null=False)
    event_description = models.TextField()
    event_venue = models.CharField(max_length=100)
    event_pic =models.FileField(max_length=100, upload_to="sports_app/pictures",default="")
    event_date= models.DateField(default=timezone.now)
    def __str__(self):#used to represent object of class event as a string
        return self.event_name

class Contact(models.Model) :
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=10,null=False)
    phone=models.CharField(max_length=10,null=False)
    user_query=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):#used to represent object of class contact as a string
        return self.name  

class Feedback_Rating(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=10,null=False)
    phone=models.CharField(max_length=10,null=False)
    feedback_text=models.TextField()
    ratings=models.CharField(max_length=6,null=False)
    date=models.DateField(default=timezone.now)
    def __str__(self):#used to represent object of class Feedback_Rating as a string
        return self.name

class User_Message(models.Model):
    receiver_id =models.CharField(max_length=40,default=None,null=False)
    sender_id =models.CharField(max_length=40,default=None,null=False)
    msg_subject =models.CharField(max_length=40,default=None,null=False)
    msg_content =models.TextField(max_length=100,null=False)
    date =models.DateField(default=timezone.now)
    receiver_status =models.BooleanField(default=True,null=True)
    sender_status =models.BooleanField(default=True,null=True)
    def __str__(self):
        return self.msg_subject

class Sport(models.Model):
    sport_name=models.CharField(max_length=10,null=False)
    no_of_players=models.IntegerField(null=False)
    equipment=models.TextField(null=False)
    description=models.TextField( null=False)
    def __str__(self):
        return self.sport_name

class Sport_Plan(models.Model):
    sport=models.ForeignKey(Sport,null=False,on_delete=models.DO_NOTHING)
    plan_name=models.CharField(max_length=20,null=False,primary_key=True)
    charge=models.IntegerField(null=False)
    facilities=models.TextField(null=False)
    def __str__(self):
        return self.plan_name

class Student(models.Model):
     student_id=models.CharField(max_length=10,null=False,primary_key=True)
     student_name=models.CharField(max_length=45,null=False)
     student_email=models.EmailField(max_length=40,null=False)
     student_password=models.CharField(max_length=20,null=False)
     student_phone=models.IntegerField(max_length=10,null=False)
     student_gender=models.CharField(max_length=10,null=False)
     student_dob= models.DateField(default=timezone.now)
     student_pic=models.FileField(max_length=100, upload_to="sports_app/student",default="")
     student_address=models.TextField(null=False)
     parent_name=models.CharField(max_length=45,null=False)
     parent_phone=models.IntegerField(max_length=10,null=False)
     def __str__(self):
         return self.student_name

class Student_Feedback(models.Model):
    std_id=models.CharField(max_length=40,default=None,null=False)
    c_id=models.CharField(max_length=40,default=None,null=False)
    feedback_text=models.TextField()
    rating=models.CharField(max_length=6,null=False)
    date=models.DateField(default=timezone.now)
    def __str__(self):
         return self.std_id
    
e_types=[('C','coach'),('T','Trainer'),('M','Medical Staff'),('S','Sweeper')]
class Employee(models.Model):
    employee_id=models.CharField(max_length=10,null=False,primary_key=True)
    employee_name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=40,null=False)
    password=models.CharField(max_length=20,null=False)
    phone=models.CharField(max_length=10,null=False)
    type=models.CharField(max_length=4,choices=e_types,null=False)
    sport=models.ForeignKey(Sport,null=True,on_delete=models.DO_NOTHING)
    experience=models.CharField(max_length=3,null=False)
    def __str__(self):
        return self.employee_name

class Tip(models.Model):
    content=models.TextField(null=False)
    employee=models.ForeignKey(Employee,null=False, on_delete=models.DO_NOTHING)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.content

class Coach_Assign(models.Model):
    student_id=models.CharField(max_length=40,default=None,null=False)
    coach_id=models.CharField(max_length=40,default=None,null=False)
    
class Sport_Suggestion(models.Model):
    name=models.CharField(max_length=40,default=None,null=False)
    weight=models.CharField(max_length=40,default=None,null=False)
    height=models.CharField(max_length=40,default=None,null=False)
    gender=models.CharField(max_length=40,default=None,null=False)
    prefered_sport=models.CharField(max_length=40,default=None,null=False)
    health_condition=models.CharField(max_length=40,default=None,null=False)
    def __str__(self):
        return self.name

class Admission_Request(models.Model):
    name=models.CharField(max_length=40,default=None,null=False)
    email=models.CharField(max_length=40,default=None,null=False)
    phone=models.CharField(max_length=40,default=None,null=False)
    gender=models.CharField(max_length=40,default=None,null=False)
    dob=models.DateField(default=timezone.now)
    height=models.CharField(max_length=40,default=None,null=False)
    weight=models.CharField(max_length=40,default=None,null=False)
    health=models.CharField(max_length=40,default=None,null=False)
    prefered_sport=models.CharField(max_length=40,default=None,null=False)
    parent_name=models.CharField(max_length=40,default=None,null=False)
    parent_phone=models.CharField(max_length=40,default=None,null=False)
    address=models.CharField(max_length=40,default=None,null=False)
    def __str__(self):
        return self.name