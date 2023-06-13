from django.shortcuts import render
from .models import User_Message,Student,Employee
from django.contrib import messages
from django.http import JsonResponse

def compose(request):
    if request.method=='GET':
        user_role=request.session["role"] #to fetch value from session
        sender_id=request.session["session_key"]
        print(user_role)
        sender_dict={"sender_key":sender_id}
        if user_role=='coach':            
            return render(request,"sports_app/coach/coach_compose.html",sender_dict)
        elif user_role=='student':            
            return render(request,"sports_app/student/student_compose.html",sender_dict)
        
    if request.method=='POST':
        s_id=request.session["session_key"]
        r_id=request.POST["receiver_id"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        r_status="True"
        s_status="True"
        #remailing values will come from control
        user_message=User_Message(receiver_id=r_id,sender_id=s_id,msg_subject=subject,msg_content=message,receiver_status=r_status,sender_status=s_status)
        user_message.save()
        user_role=request.session["role"]
        messages.success(request,"message has been sent")
        if user_role=="coach":
            return render(request,"sports_app/coach/coach_home.html")
        if user_role=="student":
            return render(request,"sports_app/student/student_home.html")
        
def inbox(request):
    if request.method=='GET':
        user_role=request.session["role"] #to fetch value from session
        rec_id=request.session["session_key"]
        message_list=User_Message.objects.filter(receiver_id=rec_id,receiver_status=True)
        message_list_dict={"msg_key":message_list}
        if user_role=="coach":
            return render(request,"sports_app/coach/coach_inbox.html",message_list_dict)
        if user_role=="student":
            return render(request,"sports_app/student/student_inbox.html",message_list_dict)

def delete_inbox_msg(request):
    if request.method=='POST':
       user_role=request.session["role"]
       rec_id=request.session["session_key"]
       delete_list=request.POST.getlist("checkid")
       for m_id in delete_list:
           m_obj=User_Message.objects.get(id=m_id)
           m_obj.receiver_status=False
           m_obj.save()
       message_list=User_Message.objects.filter(receiver_id=rec_id,receiver_status=True)
       message_list_dict={"msg_key":message_list}
       if user_role=="coach":
            return render(request,"sports_app/coach/coach_inbox.html",message_list_dict)
       if user_role=="student":
            return render(request,"sports_app/student/student_inbox.html",message_list_dict)
        
def sentmail(request):
    if request.method=='GET':
        user_role=request.session["role"] #to fetch value from session
        s_id=request.session["session_key"]
        message_list=User_Message.objects.filter(sender_id=s_id,sender_status=True)
        message_list_dict={"msg_key":message_list}
        if user_role=="coach":
                return render(request,"sports_app/coach/coach_sentmail.html",message_list_dict)
        if user_role=="student":
                return render(request,"sports_app/student/student_sentmail.html",message_list_dict) 

def delete_sentitem_msg(request):
    if request.method=='POST':
       user_role=request.session["role"]
       s_id=request.session["session_key"]
       delete_list=request.POST.getlist("checkid")
       for m_id in delete_list:
           m_obj=User_Message.objects.get(id=m_id)
           m_obj.sender_status=False
           m_obj.save()
       message_list=User_Message.objects.filter(sender_id=s_id,sender_status=True)
       message_list_dict={"msg_key":message_list}
       if user_role=="coach":
            return render(request,"sports_app/coach/coach_inbox.html",message_list_dict)
       if user_role=="student":
            return render(request,"sports_app/student/student_inbox.html",message_list_dict)

            
def validate_student_username(request):
    username=request.GET['username']
    context_dict={ 'exists':Student.objects.filter(student_id__iexact=username).exists()   }
    return JsonResponse(context_dict) 

def validate_coach_username(request):
    username=request.GET['username']
    context_dict={ 'exists':Employee.objects.filter(employee_id__iexact=username).exists()   }
    return JsonResponse(context_dict)  