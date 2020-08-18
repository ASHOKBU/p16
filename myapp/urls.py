from django.urls import path
app_name="myapp"
from myapp import views 
urlpatterns= [
    path('builtin/', views.builtinforms,name="builtinforms"), 
]