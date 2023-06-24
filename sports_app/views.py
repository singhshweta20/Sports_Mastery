from django.shortcuts import render
from .models import Event,Contact,Feedback_Rating,Sport,Sport_Plan,Employee,Student_Feedback,Tip,Sport_Suggestion,Admission_Request
from django.contrib import messages
import joblib
from sklearn.tree import DecisionTreeClassifier



##############
from xgboost import XGBClassifier
from .models import PredictedHistory
from django.core.paginator import Paginator
from .pyscrs.gitHubScrap import getUserProfile
from .pyscrs.gitHubScrap import getUsrRepo
########################################################################

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
    coach_list= Employee.objects.filter(type="C")
    event_list= Event.objects.all()
    # print(coach_list_dict)
    home_dict = {"event_key":event_list,
                 "feedback_key" :feedback_list,
                 "tips_key":tips_list,
                 "coach_list":coach_list,
                 "event_list": event_list            
                }   
    return render(request,'sports_app/html/home.html',home_dict) #passing dict to webpage

def home2(request):
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
    return render(request,'sports_app/html/home_original.html',home_dict) #passing dict to webpage


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

def statistics(request):
    return render(request,'sports_app/html/statistics.html')

def user_profile(request):
    if request.method=="GET":
        coach_list= Employee.objects.filter(type="C")
        coach_list_dict={"coach_list_key":coach_list}
        return render(request,'sports_app/html/coach.html',coach_list_dict)
    
def coach(request, id):
    emp_content= Employee.objects.get(employee_id=id)
    coach={"coach": emp_content}
    print(coach)
    return render(request,'sports_app/html/coach.html',coach)

def event(request, id):
    event_content= Event.objects.get(event_id=id)
    event={"event": event_content}
    print(event)
    return render(request,'sports_app/html/event.html', event)

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
    



############################################################################



def main(request):
    predictionHist = PredictedHistory.objects.all().order_by("-predicted_on")[:20]
    games = []
    teams_1 = []
    teams_2 = []
    results = []
    predictedTimes = []

    for predictions in predictionHist:
        games.append(predictions.game)
        teams_1.append(predictions.team_1)
        teams_2.append(predictions.team_2)
        results.append(predictions.result)
        predictedTimes.append(predictions.predicted_on)

    pred_items = zip(games, teams_1, teams_2, results, predictedTimes)

    print(pred_items)


    # full_name, usr_desc, usr_img, pinned_repositories, pinned_repo_links, pinned_repo_desc = getUserProfile("DJDarkCyber")
    repo_stars, repo_forks, repo_about = getUsrRepo("DJDarkCyber", "SportsWinnerPredictor")
    user_name = "DJDarkCyber"
    full_name, usr_desc, usr_img, pinned_repositories, pinned_repo_links, pinned_repo_desc = getUserProfile("DJDarkCyber")

    pinned_items = zip(pinned_repositories, pinned_repo_links, pinned_repo_desc)

    htmlVars = {
        "pred_items": pred_items,
        "repo_stars": repo_stars,
        "repo_forks": repo_forks,
        "repo_about": repo_about,
        "full_name": full_name,
        "user_name": user_name,
        "usr_desc": usr_desc,
        "usr_img": usr_img,
        "pinned_items": pinned_items
    } 
    return render(request, "sportsPredictor/html/index.html", htmlVars)

def predictOptions(request):
    return render(request, "sportsPredictor/html/predictOptions.html")


def predictionHistory(request):
    predictionHist = PredictedHistory.objects.all().order_by("-predicted_on")
    games = []
    teams_1 = []
    teams_2 = []
    results = []
    predictedTimes = []

    for predictions in predictionHist:
        games.append(predictions.game)
        teams_1.append(predictions.team_1)
        teams_2.append(predictions.team_2)
        results.append(predictions.result)
        predictedTimes.append(predictions.predicted_on)
    
    items = zip(games, teams_1, teams_2, results, predictedTimes)

    paginator = Paginator(list(items), 40)
    page = request.GET.get("page")
    items = paginator.get_page(page)

    htmlVars = {
        "items": items
    }


    return render(request, "sportsPredictor/html/predictionHistory.html", htmlVars)


def predictAsiaWorldCup(request):
    
    team_1s = open("data/asiaworldcup/Team_1", encoding="utf8")
    team_1s = team_1s.readlines()
    team_1s = [item.replace("\n", "") for item in team_1s]

    team_2s = open("data/asiaworldcup/Team_2", encoding="utf8")
    team_2s = team_2s.readlines()
    team_2s = [item.replace("\n", "") for item in team_2s]    

    venues = open("data/asiaworldcup/Venue", encoding="utf8")
    venues = venues.readlines()
    venues = [item.replace("\n", "") for item in venues]  

    innings_1st = open("data/asiaworldcup/1st_Innings", encoding="utf8")
    innings_1st = innings_1st.readlines()
    innings_1st = [item.replace("\n", "") for item in innings_1st]

    innings_2nd = open("data/asiaworldcup/2nd_Innings", encoding="utf8")
    innings_2nd = innings_2nd.readlines()
    innings_2nd = [item.replace("\n", "") for item in innings_2nd]


    htmlVars = {
        "team_1s": team_1s,
        "team_2s": team_2s,
        "venues": venues,
        "innings_1st": innings_1st,
        "innings_2nd": innings_2nd

    }

    return render(request, "sportsPredictor/html/predictAsiaWorldCup.html", htmlVars)

def asiaWorldCupPredictionResult(request):
    if request.method == "POST":
        team_1 = request.POST.get("TEAM1")
        team_2 = request.POST.get("TEAM2")
        venue = request.POST.get("VENUE")
        inning_1 = request.POST.get("INNING1")
        inning_2 = request.POST.get("INNING2")

        print("-------------")
        print(team_1, team_2, venue, inning_1, inning_2)

        xclf = XGBClassifier()
        xclf.load_model("data/asiaworldcup/XGBAsiaWorldCup.json")

        team_1s = open("data/asiaworldcup/Team_1", encoding="utf8")
        team_1s = team_1s.readlines()
        team_1s = [item.replace("\n", "") for item in team_1s]

        team_2s = open("data/asiaworldcup/Team_2", encoding="utf8")
        team_2s = team_2s.readlines()
        team_2s = [item.replace("\n", "") for item in team_2s]    

        venues = open("data/asiaworldcup/Venue", encoding="utf8")
        venues = venues.readlines()
        venues = [item.replace("\n", "") for item in venues]  

        innings_1st = open("data/asiaworldcup/1st_Innings", encoding="utf8")
        innings_1st = innings_1st.readlines()
        innings_1st = [item.replace("\n", "") for item in innings_1st]

        innings_2nd = open("data/asiaworldcup/2nd_Innings", encoding="utf8")
        innings_2nd = innings_2nd.readlines()
        innings_2nd = [item.replace("\n", "") for item in innings_2nd]

        won_teams = open("data/asiaworldcup/Won", encoding="utf8")
        won_teams = won_teams.readlines()
        won_teams = [item.replace("\n", "") for item in won_teams]  


        
        predictedWinner = xclf.predict([[team_1s.index(team_1), team_2s.index(team_2), venues.index(venue), innings_1st.index(inning_1), innings_2nd.index(inning_2)]])
        print([team_1s.index(team_1), team_2s.index(team_2), venues.index(venue), innings_1st.index(inning_1), innings_2nd.index(inning_2)])
        print(won_teams[predictedWinner[0]])

        won_team = won_teams[predictedWinner[0]]

        if won_team == "Tied":
            pass
        elif won_team != team_1 and won_team != team_2:
            won_team = "Error"
        
        elif team_1 == team_2:
            won_team = "Error"
        elif won_team == "No Result":
            won_team = "Error"

        htmlVars = {
            "team_1": team_1,
            "team_2": team_2,
            "won_team": won_team
        }

        del xclf


        if won_team != "Error":
            prediction = PredictedHistory(game="Asia World Cup", team_1=team_1, team_2=team_2, result=won_team)
            prediction.save()

        return render(request, "sportsPredictor/html/asiaWorldCupPredictionResult.html", htmlVars)


def predictIPL(request):
    
    team_1s = open("data/ipl/team1", encoding="utf8")
    team_1s = team_1s.readlines()
    team_1s = [item.replace("\n", "") for item in team_1s]

    team_2s = open("data/ipl/team2", encoding="utf8")
    team_2s = team_2s.readlines()
    team_2s = [item.replace("\n", "") for item in team_2s]    

    venues = open("data/ipl/venue", encoding="utf8")
    venues = venues.readlines()
    venues = [item.replace("\n", "") for item in venues]  

    toss_winners = open("data/ipl/toss_winner", encoding="utf8")
    toss_winners = toss_winners.readlines()
    toss_winners = [item.replace("\n", "") for item in toss_winners]

    toss_decisions = open("data/ipl/toss_decision", encoding="utf8")
    toss_decisions = toss_decisions.readlines()
    toss_decisions = [item.replace("\n", "") for item in toss_decisions]


    htmlVars = {
        "team_1s": team_1s,
        "team_2s": team_2s,
        "venues": venues,
        "toss_winners": toss_winners,
        "toss_decisions": toss_decisions

    }

    return render(request, "sportsPredictor/html/predictIPL.html", htmlVars)

def iplPredictionResult(request):
    if request.method == "POST":
        team_1 = request.POST.get("TEAM1")
        team_2 = request.POST.get("TEAM2")
        venue = request.POST.get("VENUE")
        toss_winner = request.POST.get("TOSSWINNER")
        toss_decision = request.POST.get("TOSSDECISION")

        print("-------------")
        print(team_1, team_2, venue, toss_winner, toss_decision)

        xclf = XGBClassifier()
        xclf.load_model("data/ipl/XGBiplModel.json")

        team_1s = open("data/ipl/team1", encoding="utf8")
        team_1s = team_1s.readlines()
        team_1s = [item.replace("\n", "") for item in team_1s]

        team_2s = open("data/ipl/team2", encoding="utf8")
        team_2s = team_2s.readlines()
        team_2s = [item.replace("\n", "") for item in team_2s]    

        venues = open("data/ipl/venue", encoding="utf8")
        venues = venues.readlines()
        venues = [item.replace("\n", "") for item in venues]  

        toss_winners = open("data/ipl/toss_winner", encoding="utf8")
        toss_winners = toss_winners.readlines()
        toss_winners = [item.replace("\n", "") for item in toss_winners]

        toss_decisions = open("data/ipl/toss_decision", encoding="utf8")
        toss_decisions = toss_decisions.readlines()
        toss_decisions = [item.replace("\n", "") for item in toss_decisions]

        won_teams = open("data/ipl/winner", encoding="utf8")
        won_teams = won_teams.readlines()
        won_teams = [item.replace("\n", "") for item in won_teams]  


        
        predictedWinner = xclf.predict([[venues.index(venue), team_1s.index(team_1), team_2s.index(team_2), toss_winners.index(toss_winner), toss_decisions.index(toss_decision)]])
        print([venues.index(venue), team_1s.index(team_1), team_2s.index(team_2), toss_winners.index(toss_winner), toss_decisions.index(toss_decision)])
        print(won_teams[predictedWinner[0]])

        won_team = won_teams[predictedWinner[0]]

        if won_team == "Tied":
            pass
        elif won_team != team_1 and won_team != team_2:
            won_team = "Error"
        
        elif team_1 == team_2:
            won_team = "Error"
        elif won_team == "No Result":
            won_team = "Error"

        htmlVars = {
            "team_1": team_1,
            "team_2": team_2,
            "won_team": won_team
        }

        del xclf


        if won_team != "Error":
            prediction = PredictedHistory(game="IPL", team_1=team_1, team_2=team_2, result=won_team)
            prediction.save()

        return render(request, "sportsPredictor/html/iplPredictionResult.html", htmlVars)

def predictT20(request):
    
    team_1s = open("data/t20/team_1", encoding="utf8")
    team_1s = team_1s.readlines()
    team_1s = [item.replace("\n", "") for item in team_1s]

    team_2s = open("data/t20/team_2", encoding="utf8")
    team_2s = team_2s.readlines()
    team_2s = [item.replace("\n", "") for item in team_2s]    

    venues = open("data/t20/venue", encoding="utf8")
    venues = venues.readlines()
    venues = [item.replace("\n", "") for item in venues]  

    toss_winners = open("data/t20/toss_winner", encoding="utf8")
    toss_winners = toss_winners.readlines()
    toss_winners = [item.replace("\n", "") for item in toss_winners]

    genders = open("data/t20/gender", encoding="utf8")
    genders = genders.readlines()
    genders = [item.replace("\n", "") for item in genders]

    toss_decisions = open("data/t20/elected_first", encoding="utf8")
    toss_decisions = toss_decisions.readlines()
    toss_decisions = [item.replace("\n", "") for item in toss_decisions]


    htmlVars = {
        "team_1s": team_1s,
        "team_2s": team_2s,
        "venues": venues,
        "toss_winners": toss_winners,
        "genders": genders,
        "toss_decisions": toss_decisions

    }

    return render(request, "sportsPredictor/html/predictT20.html", htmlVars)

def t20PredictionResult(request):
    if request.method == "POST":
        team_1 = request.POST.get("TEAM1")
        team_2 = request.POST.get("TEAM2")
        venue = request.POST.get("VENUE")
        gender = request.POST.get("GENDER")
        toss_winner = request.POST.get("TOSSWINNER")
        toss_decision = request.POST.get("TOSSDECISION")

        xclf = XGBClassifier()
        xclf.load_model("data/t20/XGBt20Model.json")

        team_1s = open("data/t20/team_1", encoding="utf8")
        team_1s = team_1s.readlines()
        team_1s = [item.replace("\n", "") for item in team_1s]

        team_2s = open("data/t20/team_2", encoding="utf8")
        team_2s = team_2s.readlines()
        team_2s = [item.replace("\n", "") for item in team_2s]    

        venues = open("data/t20/venue", encoding="utf8")
        venues = venues.readlines()
        venues = [item.replace("\n", "") for item in venues]  

        toss_winners = open("data/t20/toss_winner", encoding="utf8")
        toss_winners = toss_winners.readlines()
        toss_winners = [item.replace("\n", "") for item in toss_winners]

        genders = open("data/t20/gender", encoding="utf8")
        genders = genders.readlines()
        genders = [item.replace("\n", "") for item in genders]

        toss_decisions = open("data/t20/elected_first", encoding="utf8")
        toss_decisions = toss_decisions.readlines()
        toss_decisions = [item.replace("\n", "") for item in toss_decisions]

        won_teams = open("data/t20/result", encoding="utf8")
        won_teams = won_teams.readlines()
        won_teams = [item.replace("\n", "") for item in won_teams]  


        
        predictedWinner = xclf.predict([[genders.index(gender), team_1s.index(team_1), team_2s.index(team_2), toss_decision.index(toss_decision), toss_winners.index(toss_winner), venues.index(venue)]])
        print([genders.index(gender), team_1s.index(team_1), team_2s.index(team_2), toss_decision.index(toss_decision), toss_winners.index(toss_winner), venues.index(venue)])
        print(won_teams[predictedWinner[0]])

        won_team = won_teams[predictedWinner[0]]

        if won_team == "Tied":
            pass
        elif won_team != team_1 and won_team != team_2:
            won_team = "Error"
        
        elif team_1 == team_2:
            won_team = "Error"
        elif won_team == "No Result":
            won_team = "Error"

        htmlVars = {
            "team_1": team_1,
            "team_2": team_2,
            "won_team": won_team
        }

        del xclf


        if won_team != "Error":
            prediction = PredictedHistory(game="T20", team_1=team_1, team_2=team_2, result=won_team)
            prediction.save()

        return render(request, "sportsPredictor/html/t20PredictionResult.html", htmlVars)