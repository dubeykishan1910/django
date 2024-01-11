from django.urls import path


from . import views
urlpatterns = [

    path('',views.home, name=""),
                                        #  urls 
    path('register', views.register, name="register"),
    path('login', views.my_login, name="login"),
    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD
    
    path('dashboard', views.dashboard, name="dashboard"),
]