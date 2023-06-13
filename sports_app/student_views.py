from django.shortcuts import render,redirect
from .models import Student,Student_Feedback,Employee,Coach_Assign,Tip
from django.contrib import messages

def student_login(request):
    if request.method=="GET":
        return render(request,'sports_app/student/student_login.html')
    if request.method=="POST":
       user_id=request.POST["studentid"]
       user_pass=request.POST["studentpass"]
       #print(coach_id,coach_pass)
       student_list=Student.objects.filter(student_id=user_id,student_password=user_pass)
       l=len(student_list)
       if l>0:
        student_detail= Student.objects.get(student_id=user_id) 
        stu_context={"student_dict_key":student_detail} 
        request.session["session_key"]=user_id #binding id to session
        request.session["role"]="student"
        return render(request,'sports_app/student/student_home.html',stu_context) 
       else:
        messages.error(request,"Please enter right credentials")
        return render(request,'sports_app/student/student_login.html')
    
def student_home(request):
    if request.method=="GET":
        user_id= request.session["session_key"] #binding id to session
        student_detail= Student.objects.get(student_id=user_id)
        stu_context={"student_dict_key":student_detail } 
        return render(request,'sports_app/student/student_home.html',stu_context)

def signout(request):
    del request.session["session_key"]
    del request.session["role"]
    return redirect("student_login");

def std_feedback(request):
    if request.method=='GET': #to open html page
       user_role=request.session["role"] #to fetch value from session 
       sender_id=request.session["session_key"]
       sender_dict={"sender_key":sender_id}
       return render(request,'sports_app/student/student_feedback.html',sender_dict)
   
    if request.method=='POST':
       student_id=request.session["session_key"]
       std_name=Student.objects.get(student_id=student_id)
       coach_id=request.POST["coach_id"]
       coach_name=Employee.objects.get(employee_id=coach_id)
       feedback=request.POST["feedback"]
       rate=request.POST["rating"]
       std_feedback_obj=Student_Feedback(std_id=std_name,c_id=coach_name,feedback_text=feedback,rating=rate)
       std_feedback_obj.save()
       messages.success(request,"Thank you for your feedback. ")
       return render(request,'sports_app/student/student_feedback.html')
   
def student_edit_profile(request):
    if request.method=='GET': #to open html page 
       user_id=request.session["session_key"]
       user_detail=Student.objects.get(student_id=user_id)
       user_dict={"user_key":user_detail}
       return render(request,'sports_app/student/student_edit_profile.html',user_dict)
    if request.method=="POST":
       user_id=request.session["session_key"]
       user_name=request.POST["student_name"]
       user_email=request.POST["student_email"]
       user_password=request.POST["student_password"]
       user_phone=request.POST["student_phone"]
       user_obj=Student.objects.get(student_id=user_id)
       user_obj.student_name=user_name
    #    user_obj.student_email=user_email
    #    user_obj.student_password=user_password
    #    user_obj.student_phone=user_phone
       user_obj.save()
       user_dict={"user_key":user_obj}
       messages.error(request,"Your Details have been Changed.")
       return render(request,'sports_app/student/student_edit_profile.html',user_dict)

def student_coach(request):
    if request.method=='GET':
        s_id=request.session["session_key"]
        ca=Coach_Assign.objects.get(student_id=s_id)
        c_detail=Employee.objects.get(employee_id=ca.coach_id)
        
        student_detail= Student.objects.get(student_id=s_id)
        ca=Coach_Assign.objects.get(student_id=student_detail.student_id) 
        print(ca.coach_id)
        tips_list=Tip.objects.filter(employee=ca.coach_id)
        print(tips_list)
        c_info={"c_info_key":c_detail,
                "tips_key":tips_list}
        return render(request,"sports_app/student/student_coach.html",c_info)