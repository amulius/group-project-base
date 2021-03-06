from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from lms import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url("^$", TemplateView.as_view(template_name="index.html"), name="slides_home"),

    # Week 1 - OO Python
    url("^week1/1/$", TemplateView.as_view(template_name="week1/1.html"), name="week1_day1"),
    url("^week1/2/$", TemplateView.as_view(template_name="week1/2.html"), name="week1_day2"),
    url("^week1/3/$", TemplateView.as_view(template_name="week1/3.html"), name="week1_day3"),
    url("^week1/4_am/$", TemplateView.as_view(template_name="week1/4_am.html"), name="week1_day4_am"),
    url("^week1/4_pm/$", TemplateView.as_view(template_name="week1/4_pm.html"), name="week1_day4_pm"),

    # Week 2 - DB Intro + Introductory Django
    url("^week2/1_am/$", TemplateView.as_view(template_name="week2/1_am.html"), name="week2_day1_am"),
    url("^week2/1_pm/$", TemplateView.as_view(template_name="week2/1_pm.html"), name="week2_day1_pm"),
    url("^week2/2_am/$", TemplateView.as_view(template_name="week2/2_am.html"), name="week2_day2_am"),
    url("^week2/2_pm/$", TemplateView.as_view(template_name="week2/2_pm.html"), name="week2_day2_pm"),
    url("^week2/3_am/$", TemplateView.as_view(template_name="week2/3_am.html"), name="week2_day3_am"),
    url("^week2/3_pm/$", TemplateView.as_view(template_name="week2/3_pm.html"), name="week2_day3_pm"),
    url("^week2/4_am/$", TemplateView.as_view(template_name="week2/4_am.html"), name="week2_day4_am"),
    url("^week2/4_pm/$", TemplateView.as_view(template_name="week2/4_pm.html"), name="week2_day4_pm"),
    url("^week2/5_am/$", TemplateView.as_view(template_name="week2/5_am.html"), name="week2_day5_am"),
    url("^week2/5_pm/$", TemplateView.as_view(template_name="week2/5_pm.html"), name="week2_day5_pm"),

    # Start Project Cheatsheet
    url("^start_project_cheatsheet/$", TemplateView.as_view(template_name="start_project.html"), name="start_project"),

    # Week 3 - Introductory Django
    url("^week3/1_am/$", TemplateView.as_view(template_name="week3/1_am.html"), name="week3_day1_am"),
    url("^week3/1_pm/$", TemplateView.as_view(template_name="week3/1_pm.html"), name="week3_day1_pm"),
    url("^week3/2_am/$", TemplateView.as_view(template_name="week3/2_am.html"), name="week3_day2_am"),
    url("^week3/2_pm/$", TemplateView.as_view(template_name="week3/2_pm.html"), name="week3_day2_pm"),
    url("^week3/3_am/$", TemplateView.as_view(template_name="week3/3_am.html"), name="week3_day3_am"),
    url("^week3/3_pm/$", TemplateView.as_view(template_name="week3/3_pm.html"), name="week3_day3_pm"),
    url("^week3/lab/$", TemplateView.as_view(template_name="week3/lab.html"), name="week3_lab"),

    url(r'^test_overlay/$', 'slides.views.test_overlay', name='test_overlay'),
    url(r'^teacher/$', 'slides.views.teacher', name='teacher'),

    # User authentication
    url(r'^register/$', 'slides.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^account/$', 'slides.views.edit_account', name='edit_account'),


    url(r'^done/$', 'slides.views.done', name='done'),
    url(r'^help/$', 'slides.views.help', name='help'),
    url(r'^question/$', 'slides.views.question', name='question'),

    url(r'^teacher_index/$', 'slides.views.teacher_index', name='teacher_index'),
    url(r'^lecture_fragment/$', 'slides.views.lecture_fragment', name='lecture_fragment'),
    url(r'^details/$', 'slides.views.details', name='details'),

    url(r'^update/$', 'slides.views.update', name='update'),

    url(r'^student_actions/$', 'slides.views.student_actions', name='student_actions'),
    url(r'^teacher/week(?P<week_number>\d+)/(?P<lecture_time>.+)/$', 'slides.views.lecture', name="lecture"),
    url(r'^done/week(?P<week_number>\d+)/(?P<lecture_time>.+)/$', 'slides.views.done_test', name="done_test"),
    url(r'^help/week(?P<week_number>\d+)/(?P<lecture_time>.+)/$', 'slides.views.help_test', name="help_test"),
    url(r'^question/week(?P<week_number>\d+)/(?P<lecture_time>.+)/$', 'slides.views.question_test', name="question_test"),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)