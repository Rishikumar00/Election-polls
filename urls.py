from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:question_text>/', views.DetailView.as_view(), name='detail'),
    path('<str:question_text>/results/', views.ResultsView.as_view(), name='results'),
    path('<str:question_text>/vote/', views.vote, name='vote'),
]

