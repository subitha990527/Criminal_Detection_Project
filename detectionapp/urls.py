from django.urls import path
from detectionapp import views, admin_views, police_views, public_views

urlpatterns = [
    path("",views.home,name="home"),
    path("loginpage",views.loginpage,name="loginpage"),
    path("loginpage", views.loginpage, name="loginpage"),


    #################  admin  ###################

    path("adminpage",admin_views.adminpage,name="adminpage"),
    path("registrationpage",admin_views.registrationpage,name="registrationpage"),
    path("police_view1",admin_views.police_view1,name="police_view1"),
    path("removepolice/<int:id>/",admin_views.removepolice,name='removepolice'),
    path("updatepolice/<int:id>/",admin_views.updatepolice,name='updatepolice'),
    path("public_view",admin_views.public_view,name="public_view"),
    path("removepublic/<int:id>/",admin_views.removepublic,name='removepublic'),
    path("criminalregpage",admin_views.criminalregpage,name="criminalregpage"),
    path("criminal_view", admin_views.criminal_view,name="criminal_view"),
    path("removecriminal/<int:id>/", admin_views.removecriminal, name='removecriminal'),
    path("updatecriminal/<int:id>/", admin_views.updatecriminal, name='updatecriminal'),
    path("missing_view2", admin_views.missing_view2, name="missing_view2"),
    path("removemissing1/<int:id>/", admin_views.removemissing1, name='removemissing1'),
    path("updatemissing1/<int:id>/", admin_views.updatemissing1, name='updatemissing1'),
    path("complaint_view1", admin_views.complaint_view1, name="complaint_view1"),
    path("notificationpage", admin_views.notificationpage, name="notificationpage"),
    path("notify_view", admin_views.notify_view, name="notify_view"),
    path("removenotify/<int:id>/",admin_views.removenotify,name='removenotify'),
    path("updatenotify/<int:id>/",admin_views.updatenotify,name='updatenotify'),



                        ########################   police   #################################



    path("policepage",police_views.policepage,name="policepage"),
    path("addmissingpage",police_views.addmissingpage,name="addmissingpage"),
    path("missing_view", police_views.missing_view, name="missing_view"),
    path("removemissing/<int:id>/", police_views.removemissing, name='removemissing'),
    path("updatemissing/<int:id>/", police_views.updatemissing, name='updatemissing'),
    path("criminal_view1", police_views.criminal_view1, name="criminal_view1"),
    path("complaint_view", police_views.complaint_view, name="complaint_view"),
    path("police_profile", police_views.police_profile, name="police_profile"),
    path("editprofile/<int:id>/", police_views.editprofile, name="editprofile"),
    path("reply_complaint/<int:id>/",police_views.reply_complaint,name='reply_complaint'),
    path("notify_view1", police_views.notify_view1, name="notify_view1"),
    path("detection_view", police_views.detection_view, name="detection_view"),


###########################   public   ########################


    path("public_page",public_views.publicpage,name="public_page"),
    path("publicregpage", public_views.publicregpage, name="publicregpage"),
    path("missing_view1", public_views.missing_view1, name="missing_view1"),
    path("criminal_view2", public_views.criminal_view2, name="criminal_view2"),
    path("complaintpage", public_views.complaintpage, name="complaintpage"),
    path("complaint_view2", public_views.complaint_view2, name="complaint_view2"),
    path("public_profile", public_views.public_profile, name="public_profile"),
    path("editpublicprofile/<int:id>/", public_views.editpublicprofile, name="editpublicprofile"),
    path("notify_view2", public_views.notify_view2, name="notify_view2"),
    path("detect", public_views.detect, name="detect"),
    path("det", public_views.det, name="det"),
    path("detectionpage",public_views.detectionpage,name="detectionpage")























]