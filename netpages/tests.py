from django.test import TestCase

# Create your tests here.
from datetime import datetime,date

from django.db import models

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GWYM.settings")

import django
django.setup()

def main():

    from models import Article

    atc = Article()
    act.acticle_title = "批量导入实例1"
    act.article_content = "内容——没有进行 字段优化的内容"
    act.article_cate = 1
    act.commit_date = datetime.now().date()

    img = 'C:\\Users\\lenovo\\Desktop\\pic\\demo.png'
    act.article_img.save('demo.png',img, save=True)

    Article.objects.get_or_create(act)
    img.close()

    print ("已存储")

if __name__ == "__main__":
    main()
    print('Done!')
