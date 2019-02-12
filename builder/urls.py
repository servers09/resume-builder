from django.urls import path, include
from . import views

app_name = 'builder'
urlpatterns = [
    path('edit/user_id=<int:id>/', views.ResumeEdit.as_view(),name='edit'),
    path('preview/user_id=<int:id>/', views.GeneratePdf.as_view(),name='preview'),
    path('choose/', views.Choose.as_view(),name='choose'),
    ]