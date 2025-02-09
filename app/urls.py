from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name="home"),

    #user
    path('user_list', views.user_list_view, name="user_list"),
    path('user_add', views.user_add_view, name='user_add'),
    path("user_form", views.user_form, name="user_add"),
    path("user_form/<int:id>", views.user_form, name="user_update"), 
    path('user_del/<id>', views.user_del, name = 'user_del'),


    #project
    path('project_list', views.project_list_view, name="project_list"),
    # path("project_form", views.project_form, name="project_form"),
    # path("project_form/<int:id>", views.project_form, name="project_update"),

    #vocative
    path('vocative_list', views.vocative_list_view, name="vocative_list"),
    # path("vocative_form", views.user_form, name="vocative_form"),
    # path("vocative_form/<int:id>", views.user_form, name="vocative_update"),

    #delegate
    path('delegate_list', views.delegate_list_view, name="delegate_list"),
    # path("delegate_form", views.delegate_form, name="delegate_form"),
    # path("delegate_form/<int:id>", views.delegate_form, name="delegate_update"),

    #notification
    path('notification_list', views.notification_list_view, name="notification_list"),
    # path("notification_form", views.notification_form, name="notification_form"),
    # path("notification_form/<int:id>", views.notification_form, name="notification_update"),

    #address
    path('address_list', views.address_list_view, name="address_list"),
    # path("address_form", views.address_form, name="address_form"),
    # path("address_form/<int:id>", views.address_form, name="address_update"),


    #investment
    path('investment_list', views.investment_list_view, name="investment_list"),
    # path("investment_form", views.investment_form, name="investment_form"),
    # path("investment_form/<int:id>", views.investment_form, name="investment_update"),


    #event
    path('event_list', views.event_list_view, name="event_list"),
    # path("event_form", views.event_form, name="event_form"),
    # path("event_form/<int:id>", views.event_form, name="event_update"),




]