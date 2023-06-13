from django.shortcuts import render
from .models import Event,Contact,Feedback_Rating,Sport,Sport_Plan,Employee,Student_Feedback,Tip,Sport_Suggestion,Admission_Request
from django.contrib import messages
import joblib
from sklearn.tree import DecisionTreeClassifier

# Create your views here.
def test(request):
    return render(request,"sports_app/coach/coach_test.html"
                  )
def home(request):
    event_list= Event.objects.all() #to fetch ojects of table
    feedback_list=Student_Feedback.objects.all() 
       
    tips_list=Tip.objects.all()
    # for t in tips_list:
    #     print(t.content)
    #     print( t.employee)
    
    home_dict = {"event_key":event_list,
                 "feedback_key" :feedback_list,
                 "tips_key":tips_list              
                }   
    return render(request,'sports_app/html/home.html',home_dict) #passing dict to webpage

def feedback(request):
    if request.method=='GET': #to open html page 
       return render(request,'sports_app/html/feedback.html')
    if request.method=='POST':
       user_name=request.POST["name"]#requst.POST is dict and name is is th key
       user_email=request.POST["email"]
       user_phone=request.POST["phone"]
       user_feedback=request.POST.get("feedback")
       user_rating=request.POST["ratings"]
       feedback_obj=Feedback_Rating(name=user_name, email=user_email, phone=user_phone, feedback_text=user_feedback,ratings=user_rating)
       feedback_obj.save()#to save data in feedback table
       print("data saved")
       messages.success(request,"Thank you for your feedback, we will reach you soon!!!")
       return render(request,'sports_app/html/feedback.html')
       


def aboutus(request):
    return render(request,'sports_app/html/aboutus.html')

def contactus(request):
    if request.method=='GET': #to open html page 
       return render(request,'sports_app/html/contactus.html')
    if request.method=='POST':
       user_name=request.POST["name"]#requst.POST is dict and name is is th key
       user_email=request.POST["email"]
       user_phone=request.POST["phone"]
       user_query=request.POST.get("query")
       contact=Contact(name=user_name, email=user_email, phone=user_phone, user_query=user_query)#creating object
       contact.save()#to save data in contact table
       print("data saved")
       messages.success(request,"Thank you for contacting us, we will reach you soon!!!")
       return render(request,'sports_app/html/contactus.html')
   
def sports(request):
    if request.method=="GET":
        sports_list=Sport.objects.all()
        sports_dict={"sports_key":sports_list}
        return render(request,'sports_app/html/sports.html',sports_dict)
   
def sports_plan(request):
    if request.method=="GET":
        sports_plan_list=Sport_Plan.objects.all()
        sports_plan_dict={"sports_plan_key":sports_plan_list}
        return render(request,'sports_app/html/sports_plan.html',sports_plan_dict)

def coach(request):
    if request.method=="GET":
        coach_list= Employee.objects.filter(type="C")
        coach_list_dict={"coach_list_key":coach_list}
        return render(request,'sports_app/html/coach.html',coach_list_dict)
    
def sport_suggestion(request):
    if request.method=="GET":
        return render(request,'sports_app/html/sport_suggestion.html')
    
    if request.method=="POST":
        u_name=request.POST["name"]
        u_weight=request.POST["weight"]
        u_height=request.POST["height"]
        u_gender=request.POST["gender"]
        sport=request.POST["prefered_sport"]
        health=request.POST["health_condition"]
        
        mlModel=joblib.load("models/sports_mastry.joblib")
        prediction=mlModel.predict([[u_weight,u_height,health]])
        print(prediction)
        suggestion_obj=Sport_Suggestion(name=u_name,weight=u_weight,height=u_height,gender=u_gender,prefered_sport=sport,health_condition=health)
        suggestion_obj.save()
        messages.success(request," Best suited sport for you is "+prediction)
        return render(request,'sports_app/html/sport_suggestion.html')
    
def view_contents(request,id):
    # print(id)
    event_obj= Event.objects.get(id=id)
    event_dict={"event_key":event_obj}
    return render(request,"sports_app/html/view_event.html",event_dict)

def admission_request(request):
    if request.method=="GET":
        return render(request,'sports_app/html/admission_request.html')
    
    if request.method=="POST":
        s_name=request.POST["name"]
        s_email=request.POST["email"]
        s_phone=request.POST["phone"]
        s_gender=request.POST["gender"]
        s_dob=request.POST["dob"]
        s_height=request.POST["height"]
        s_weight=request.POST["weight"]
        s_health=request.POST["health"]
        s_prefered_sport=request.POST["prefered_sport"]
        s_parent_name=request.POST["parent_name"]
        s_parent_phone=request.POST["parent_phone"]
        s_address=request.POST["address"]
        s_obj=Admission_Request(name=s_name,email=s_email,phone=s_phone,
                                gender=s_gender,dob=s_dob,height=s_height,
                                weight=s_weight,health=s_health,
                                prefered_sport=s_prefered_sport,parent_name=s_parent_name,
                                parent_phone=s_parent_phone,address=s_address)
        s_obj.save() 
        messages.success(request,"Admission Request Sent Successfully")      
        return render(request,'sports_app/html/admission_request.html')