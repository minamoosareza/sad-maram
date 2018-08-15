from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='post_list'),#todo change to the homepage
    url(r'^upload_file$', views.upload_file, name='upload_file'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^ch_pass$', views.bala_pass, name='bala_pass'),
    url(r'^edit_user_profile$', views.edit_user_profile, name='edit_user_profile'),
    url(r'^change_pass$', views.change_pass, name='change_pass'),
    url(r'^bala_add_employee$', views.bala_add_employee, name='bala_add_employee'),
    url(r'^add_employee$', views.add_employee, name='add_employee'),
    url(r'^employee_list$', views.employee_list, name='employee_list'),
    url(r'^(?P<pke>\d+)/empProfile$', views.see_employee_profile, name='see_employee_profile'),
    url(r'^(?P<pke>\d+)/change_salaryyy$', views.bala_change_employee_salary, name='change_empsalary'),
    url(r'^(?P<pke>\d+)/change_salary$', views.change_salary, name='change_salary'),
    url(r'^(?P<pke>\d+)/emp_transactions$', views.see_employee_transactions, name='see_employee_transactions'),
    url(r'^(?P<pkt>\d+)/emp_transactions_context$', views.see_transaction_context, name='see_transaction_context'),

    url(r'^nerkh_arz$', views.nerkh_arz, name='nerkh_arz'),
    path('contactus', views.contactus, name='contactus'),
    path('managertransactions', views.managertransactions, name='managertransactions'),
    path('employeetransactions', views.employeetransactions, name='employeetransactions'),
    path('usertransactions/<int:pk>/', views.usertransactions, name='usertransactions'),
    path('waitingtransactions', views.waitingtransactions, name='waitingtransactions'),
    path('message/<int:pk>/', views.message, name='message'),
    path('transaction/<int:pk>/', views.transaction, name='transaction'),
    path('gre', views.gre, name='gre'),
    path('toefl', views.toefl, name='toefl'),
    path('ielts', views.ielts, name='ielts'),
    path('inform/<int:pk>/', views.inform, name='inform'),
    path('yes/<int:pk>/', views.yes, name='yes'),
    path('no/<int:pk>/', views.no, name='no'),
    path('accept/<int:pk>/', views.accept, name='accept'),
    path('runtransactions/<int:pk>/', views.runtransactions, name='runtransactions'),
    path('transaction/<int:pk>/', views.transaction, name='transaction'),
]
