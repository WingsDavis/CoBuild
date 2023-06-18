from django.urls import path
from . import views

urlpatterns = [
    path('module/', views.module, name = 'module'),
    path('project/<str:pk>/', views.project, name = 'project'),
    path('create/',views.Create, name = 'create'),
    path('update/<str:pk>/',views.Update, name = 'update'),
    path('delete/<str:pk>/',views.Delete, name = 'delete'),
    path('credlogin/', views.CredLogin, name = 'credlogin'),
    path('credlogout/', views.CredLogout, name = 'credlogout'),
    path('crednewuser/', views.CredNewUser, name = 'crednewuser'),
    path('clearchat/<str:pk>/',views.ClearChat, name = 'clearchat'),
    path('useraccount/<str:pk>/', views.UserAccount, name = 'useraccount')
    
]
