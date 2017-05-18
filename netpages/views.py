from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.template import loader
from netpages.models import Article,Top3p

# Create your views here.

def home_all_set():
    posts1 = [x for x in Article.objects.all() if x.article_cate == int(1)][0:8]#news_center  8
    posts2 = [x for x in Article.objects.all() if x.article_cate == 2][0:5]##indu_info  5
    posts3 = [x for x in Article.objects.all() if x.article_cate == 3][0:6]#product_show
    posts4 = [x for x in Article.objects.all() if x.article_cate == 4][0]#produ_serv
    posts5 = [x for x in Article.objects.all() if x.article_cate == 5][0:2]#acti_theme
    posts6 = [x for x in Article.objects.all() if x.article_cate == 6][0] #aboutme

    return posts1,posts2,posts3,posts4,posts5,posts6

def add3Pic(request):

    return render(request, "")

def pages(cate):
    #als = Article.objects.all()
    gaims = [x for x in Article.objects.all() if x.article_cate == int(cate)]
    # pre the page_num for the pages
    pages = [int(len(gaims)/5)-1 if len(gaims)%5==0 else int(len(gaims)/5)][0]
    # set the sum(pages)[] for pages
    i_pages = [i+1 for i in range(pages+1)] # how many pages need to show in html
    # set urls for the cate_ split_pages
    urls = ['demo_'+str(cate)+"_"+str(i) for i in i_pages]

    return urls


def home(request):
    ps1, ps2, ps3, ps4,ps5, ps6 = home_all_set()

    pics = Top3p.objects.all()
    pic3 = [x.img for x in pics][0:3]
    #pis = {'p1': pic3[0], 'p2': pic3[1], 'p3': pic3[2]}
    p1 =  pic3[0]
    p2 =  pic3[1]
    p3 =  pic3[2]

    return render(request, "index_base.html" ,
                  {'ps1': ps1, 'ps2':ps2, 'ps3':ps3, 'ps4':ps4,
                        'ps5':ps5, 'ps6':ps6 ,'p1':p1,'p2':p2,'p3':p3})

def home1(request):

    return render(request,"403.html",{})

def set3Pic():
	pic3 = [x.img for x in Top3p.objects.all()][0:3]
	#pis = {'p1': pic3[0], 'p2': pic3[1], 'p3': pic3[2]}
	return pic3[0], pic3[1], pic3[2]


def set_page2(cate_id):
    As = Article.objects.all()
    ls = [x for x in As if x.article_cate == int(cate_id)]

    first_post = ls[0]
    cate = first_post.article_belongs()
    if(len(ls) <5):
        posts = ls[1:len(ls)]
    else:
        posts = ls[1:5]

    pages = [int(len(ls) / 5) - 1 if len(ls) % 5 == 0 else int(len(ls) / 5)][0]
    # set the sum(pages)[] for pages
    i_pages = [i + 1 for i in range(pages + 1)]  # how many pages need to show in html
    # set urls for the cate_ split_pages
    urls = ['demo_' + str(cate_id) + "_" + str(i) for i in i_pages]

    return first_post, posts, cate, urls

def news_center(request):
    first_post,posts,cate,urls = set_page2(1)
    p1,p2,p3 = set3Pic()
    return render(request, "undertake_page.html",
                  {'posts':posts, 'first_post':first_post, 'cate':cate, 'urls':urls, 'p1':p1, 'p2':p2,'p3':p3})

def industry_info(request):
    first_post, posts, cate, urls = set_page2(2)
    p1, p2, p3 = set3Pic()
    return render(request, "undertake_page.html",
                  {'posts': posts, 'first_post': first_post, 'cate': cate, 'urls': urls, 'p1': p1, 'p2': p2, 'p3': p3})


def product_show(request):
    first_post, posts, cate, urls = set_page2(3)
    p1, p2, p3 = set3Pic()
    return render(request, "undertake_page.html",
                  {'posts': posts, 'first_post': first_post, 'cate': cate, 'urls': urls, 'p1': p1, 'p2': p2, 'p3': p3})


def product_and_service(request):
    first_post, posts, cate, urls = set_page2(4)
    p1, p2, p3 = set3Pic()
    return render(request, "undertake_page.html",
                  {'posts': posts, 'first_post': first_post, 'cate': cate, 'urls': urls, 'p1': p1, 'p2': p2, 'p3': p3})


def activity_theme(request):
    first_post, posts, cate, urls = set_page2(5)
    p1, p2, p3 = set3Pic()
    return render(request, "undertake_page.html",
                  {'posts': posts, 'first_post': first_post, 'cate': cate, 'urls': urls, 'p1': p1, 'p2': p2, 'p3': p3})


def page_detail(request, pid):
    gaim = [x for x in Article.objects.all() if x.id == int(pid)][0]
    first_post = gaim
    cate_id = gaim.article_cate
    cate = gaim.article_belongs()
    ls = [x for x in Article.objects.all() if x.article_cate == cate_id]
    posts = [x for x in ls if x.id != int(pid)][0:4]

    p1,p2,p3 = set3Pic()
    return render(request, "detail_base.html", {'posts':posts, 'first_post':first_post, 'cate':cate, 'p1':p1, 'p2':p2,'p3':p3})

def about_us(request):
    first_post, posts, cate, urls = set_page2(6)
    p1, p2, p3 = set3Pic()
    return render(request, "undertake_page.html",
                  {'posts': posts, 'first_post': first_post, 'cate': cate, 'urls': urls, 'p1': p1, 'p2': p2, 'p3': p3})


def set_index3p(request):
    pics = Top3p.objects.all()
    pic3 = [x.img for x in pics][0:3]
    pis = {'p1':pic3[0],'p2':pic3[1],'p3':pic3[2]}
    return render(request, "index_base.html", pis)

def set_pages(request, cate, page):
    #als = Article.objects.all()
    gaims = [x for x in Article.objects.all() if x.article_cate == int(cate)]
    # pre the page_num for the pages
    pages = [int(len(gaims)/5)-1 if len(gaims)%5==0 else int(len(gaims)/5)][0]
    # set the sum(pages)[] for pages
    i_pages = [i+1 for i in range(pages+1)] # how many pages need to show in html
    # set the start-end pages_num
    i_page_start = 5*(int(page)-1) + 1
    if i_page_start + 4 < len(gaims):
        i_page_end = i_page_start + 4
    else:
        i_page_end = len(gaims)
    # first_post and the posts
    first_post = gaims[i_page_start-1]
    posts = gaims[i_page_start:i_page_end]
    # set urls for the cate_ split_pages
    urls = ['demo_'+str(cate)+"_"+str(i) for i in i_pages]
    # I have forget the 3Index pic then add it
    p1, p2, p3 = set3Pic()

    i = int(page) #input is a int// and forloop is a int too!!!
    return render(request, "split_undertake_page.html", {'posts':posts, 'first_post':first_post, 'cate':cate,
                                                         'p1':p1, 'p2':p2, 'p3':p3,
                                                        'urls':urls ,'i':i})



