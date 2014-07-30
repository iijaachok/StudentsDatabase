from django.conf.urls import patterns, include, url

from django.contrib import admin
from StudentsListing import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StudentsDatabase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # base
    url(r'^$', views.index, name='index'),

    #Groups
    url(r'^group/list_students/(?P<group_id>\d+)/$', 'StudentsListing.views.list_students', name='list_students'),
    url(r'^group/add/$', 'StudentsListing.views.group_manager', name='add_group'),
    url(r'^group/edit/(?P<group_id>\d+)/$', 'StudentsListing.views.group_manager', name='edit_group'),
    url(r'^group/delete/(?P<group_id>\d+)/$', 'StudentsListing.views.delete_group', name='delete_group'),

    #Sturents
    url(r'^student/add/$', 'StudentsListing.views.student_manager', name='add_student'),
    url(r'^student/edit/(?P<student_id>\d+)/$', 'StudentsListing.views.student_manager', name='edit_student'),
    url(r'^student/delete/(?P<student_id>\d+)/$', 'StudentsListing.views.delete_student', name='delete_student'),

    #Account
    url(r'^login/$', 'django.contrib.auth.views.login', {"template_name": "login.html"}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
