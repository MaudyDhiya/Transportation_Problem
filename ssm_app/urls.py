from django.urls import path
from ssm_app.views import *
urlpatterns = [
    path('', home_beranda, name='home_beranda'),
    path('ssm/', home_ssm, name='home_ssm'),
    path('ksam', home_ksam, name='home_ksam'),
    path('submitssm', home_submitssm, name='home_submitssm'),
    path('submitksam', home_submitksam, name='home_submitksam'),
    path('resultksam', home_resultksam, name='home_resultksam')
]