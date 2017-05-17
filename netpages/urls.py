from django.conf.urls import *
from django.contrib import admin
from . import views

app_name = 'netpages'
urlpatterns = [
    url(r'^$', views.home, name='index_base'),

    ##set the first J pages
    url(r'newscenter$', views.news_center, name="news_center"),
    url(r'industryinfo$', views.industry_info, name="industry_index") ,
    url(r'productshow$', views.product_show, name="product_show"),
    url(r'productandservice$', views.product_and_service, name="detail_base"),
    url(r'activitytheme$', views.activity_theme, name="detail_base"),
    url(r'aboutus$', views.about_us, name="detail_base"),
    ## set the detail of every page1
    url(r'^demo2$', views.news_center, name="undertake_page"),
    url(r'^(?P<pid>\d+)$', views.page_detail , name = "PageDetail"),
	
	url(r'^demo_(?P<cate>\d+)_(?P<page>\d+)$', views.set_pages, name="TestFenYe"),
]
