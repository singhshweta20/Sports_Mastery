from django.shortcuts import render,redirect
from .models import Employee,Coach_Assign,Student,Student_Feedback,Tip
from django.contrib import messages

def coach_login(request):
    if request.method=="GET":
       return render(request,'sports_app/coach/coach_login.html')
    if request.method=="POST":
       coach_id=request.POST["coachid"]
       coach_pass=request.POST["coachpass"]
       #print(coach_id,coach_pass)
       coach_list=Employee.objects.filter(employee_id=coach_id,password=coach_pass)
       l=len(coach_list)
       if l>0:
        coach_detail= Employee.objects.get(employee_id=coach_id) 
        context={"coach_dict_key":coach_detail} 
        request.session["session_key"]=coach_id #binding id to session
        request.session["role"]="coach"        
        return render(request,'sports_app/coach/coach_home.html',context) 
       else:
        messages.error(request,"Please enter right credentials")
        return render(request,'sports_app/coach/coach_login.html')
    
def coach_home(request):
    if request.method=="GET":
        coach_id=request.session["session_key"]
        coach_detail= Employee.objects.get(employee_id=coach_id) 
        context={"coach_dict_key":coach_detail} 
        return render(request,'sports_app/coach/coach_home.html',context)

def coach_student(request):
    if request.method=="GET":
       c_id=request.session["session_key"]
       st_list=Coach_Assign.objects.filter(coach_id=c_id) #list of student assigned to 
       student_list=[]
       for s in st_list:
            s_detail=Student.objects.get(student_id=s.student_id) #detail of one student
            student_list.append(s_detail)       
       s_info={"s_list_key":student_list}       
       return render(request,"sports_app/coach/coach_student.html",s_info)

def signout(request):
    del request.session["session_key"]
    del request.session["role"]
    return redirect("coach_login");

def coach_feedback(request): #feedback of the coach
    if request.method=="GET":
        c_id=request.session["session_key"]
        c_name=Employee.objects.get(employee_id=c_id)
        feedback_list=Student_Feedback.objects.filter(c_id=c_name)
        print(feedback_list)
        f_empty_list=[]
        for s in feedback_list:
            feedback=Student_Feedback.objects.get(c_id=s.c_id)
            f_empty_list.append(feedback)             
        feedback_list_dict={"feedback_list_key":f_empty_list}
        return render(request,"sports_app/coach/coach_feedback.html",feedback_list_dict) 
    
def coach_edit_profile(request):
    if request.method=="GET":
        coach_id=request.session["session_key"]
        print( coach_id )
        coach_obj= Employee.objects.get(employee_id=coach_id) 
        coach_detail={"coach_key":coach_obj} 
        return render(request,'sports_app/coach/coach_edit_profile.html',coach_detail)
    if request.method=="POST":
        coach_id=request.session["session_key"]
        coach_email=request.POST["coach_email"]
        coach_password=request.POST["coach_password"]
        coach_phone=request.POST["coach_phone"]
        coach_experience=request.POST["coach_experience"]
        coach_obj=Employee.objects.get(employee_id=coach_id)
        coach_obj.email=coach_email
        coach_obj.password=coach_password
        coach_obj.phone=coach_phone
        coach_obj.experience=coach_experience
        coach_obj.save()
        coach_detail={"coach_key":coach_obj} 
        messages.error(request,"Your Details have been Changed.")
        return render(request,'sports_app/coach/coach_edit_profile.html',coach_detail)
    
def coach_tip(request):
    if request.method=="GET":
       coach_id=request.session["session_key"]
       coach_obj= Employee.objects.get(employee_id=coach_id) 
       coach_dict={"coach_key":coach_obj}
       return render(request,'sports_app/coach/coach_tip.html',coach_dict) 

    if request.method=="POST":
       user_id=request.session["session_key"]
       user=Employee.objects.get(employee_id=user_id)
       tip=request.POST["content"]
       tip_obj=Tip(content=tip,employee=user)
       tip_obj.save()
    #    tip_dict={"tip_key",tip_obj}
       return render(request,'sports_app/coach/coach_tip.html')