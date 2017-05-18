# -*- coding: utf-8 -*-
# Create your tests here.
from datetime import datetime,date

from django.db import models

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GWYM.settings")

import django
django.setup()

def main():


    from netpages.models import Article

    #img = open('D:\\net_pages\\static\\netpages\\img\\self.png','rb+')
    #img = 'C:\\Users\\lenovo\\Desktop\\pic\\demo.png'
    a = [('tittle', 'content', 'C:\\Users\\lenovo\\Desktop\\pic\\demo.png', 1, datetime.now().date())]

    print (a)
    Article.objects.create(a)
    '''
Article.objects.bulk_create(
        acticle_title = 'fdsafdsa',
        article_content = "cesifdsalkfjdsafjkdsajfkdsaflkdsahfdsakjfhdsakjfhdsjfd",
        article_cate = 1,
        commit_date = datetime.now().date(),
        article_img = 'D:\\net_pages\\static\\netpages\\img\\self.png',
    )


    '''
    print ("已存储")

def mysql():
    import pymysql
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='112233..',
        db='articles_db',
    )
    cur = conn.cursor()
    cur.execute('''
            select * from netpages_article;
        ''')

    for row in cur.fetchall():
        print("No")
        print(row)

    print('Done!')

from numpy.random import randint

def test():
    from netpages.models import Article
    for i in range(200):

        cate = randint(6)+1
        author = "作者" + str(cate)
        title = "测试用例" + str(i)
        content = "<p> HTML 测试内容 </p>"
        date = datetime.today().date()
        img = "demo.jpg"

        Article.objects.create(acticle_title = title,
                    article_author = author,
        article_cate = cate,
        article_content = content,
        article_img = img,
        commit_date = date)

    print("导入完成")

if __name__ == "__main__":
    test()