from django.urls import path
from . import views,student_views,coach_views,message_views
urlpatterns = [path("",views.home,name="home"),
               path("home2/",views.home2,name="home2"),
               path("aboutus/",views.aboutus,name="aboutus"),
               path("contactus/",views.contactus,name="contactus"),
               path("feedback/",views.feedback,name="feedback"),
               path("sport_suggestion/",views.sport_suggestion,name="sport_suggestion"),
               path("admission_request/",views.admission_request,name="admission_request"),
               path("view_contents/<int:id>",views.view_contents,name=""),
               path("sports/",views.sports,name="sports"),
               path("sports_plan/",views.sports_plan,name="sports_plan"),
               path("statistics/",views.statistics,name="statistics"),
               path("coach/<id>/",views.coach,name="coach"),
               path("event/<id>/",views.event,name="event"),
               path("compose/",message_views.compose,name="compose"),
               path("inbox/",message_views.inbox,name="inbox"),
               path("sentmail/",message_views.sentmail,name="sentmail"),
               path("delete_inbox_msg/",message_views.delete_inbox_msg,name="delete_inbox_msg"),
               path("delete_sentitem_msg/",message_views.delete_sentitem_msg,name="delete_sentitem_msg"),
                              
               path("student_login/",student_views.student_login, name="student_login" ),
               path("student_home/",student_views.student_home,name="student_home"),
               path("student_feedback/",student_views.std_feedback,name="student_feedback"),
               path("student_coach/",student_views.student_coach,name="student_coach"),
               path("student_edit_profile/",student_views.student_edit_profile,name="student_edit_profile"),
               path("signout/",student_views.signout,name="signOut"),
                             
               path("coach_login/",coach_views.coach_login, name="coach_login" ),
               path("coach_home/",coach_views.coach_home,name="coach_home"),
               path("coach_student/",coach_views.coach_student,name="coach_student"),
               path("coach_feedback/",coach_views.coach_feedback,name="coach_feedback"),
               path("coach_edit_profile/",coach_views.coach_edit_profile,name="coach_edit_profile"),
               path("coach_tip/",coach_views.coach_tip,name="coach_tip"),
               path("signout/",coach_views.signout,name="signOut"),
               path("test/",views.test,name="test" ), 
               path("validate_student_username/",message_views.validate_student_username,name="validate_student_username"),
               path("validate_coach_username/",message_views.validate_coach_username,name="validate_coach_username"),





                path("prediction", views.main, name="index"),
                path("choose", views.predictOptions, name="predictOptions"),
                path("predictionHistory", views.predictionHistory, name="predictionHistory"),
                path("predictAsiaWorldCup", views.predictAsiaWorldCup, name="predictAsiaWorldCup"),
                path("asiaWorldCupPredictionResult", views.asiaWorldCupPredictionResult, name="asiaWorldCupPredictionResult"),
                path("predictIPL", views.predictIPL, name="predictIPL"),
                path("iplPredictionResult", views.iplPredictionResult, name="iplPredictionResult"),
                path("predictT20", views.predictT20, name="predictT20"),
                path("t20PredictionResult", views.t20PredictionResult, name="t20PredictionResult"),


              ]
