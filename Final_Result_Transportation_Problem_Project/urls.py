from django.urls import path
from Final_Result_Transportation_Problem_Project.views import *
urlpatterns = [
    path('', home_beranda, name='home_beranda'),
    path('ssm/', home_ssm, name='home_ssm'),
    path('ksam', home_ksam, name='home_ksam'),
    path('submitssm', home_submitssm, name='home_submitssm'),
    path('submitksam', home_submitksam, name='home_submitksam'),
    path('resultksam', home_resultksam, name='home_resultksam'),
    path('resultssm', home_resultssm, name='home_resultssm')
    
]