from django.conf.urls import url
from .models import Company, Employee
from . import views

app_name = "polls"
urlpatterns = [
    url(r'^$', views.generic_list, {'model': Company}, name='companyList'),
    url(r'^(?P<pk>[0-9]+)/$', views.company_detail_view,{'model': Company},  name='companyDetail'),
    #url(r'^list/$', , name='genericList'),
    #url(r'^(?P<pk>[0-9]+)/$', views.company_detail_view, name='companyDetail'),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.employee_detail_view, name='employeeDetail'),
    url(r'^(?P<pk>[0-9]+)/updateCompany$', views.update_company, name='updateCompany'),
    url(r'^employee/(?P<pk>[0-9]+)/updateEmployee$', views.update_employee, name='updateEmployee'),
    url(r'^company/(?P<pk>[0-9]+)/delete$', views.delete, name='deleteCompany')

    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='vote')
]



