# Create your models here.
from django.db import models

from ckeditor.fields import RichTextField

import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

class Article(models.Model):
	
    acticle_title = models.CharField(max_length=200)
    article_content = RichTextField("content")
    article_img = models.ImageField(upload_to='pic', default=".\media\pic\demo.png")
    article_cate = models.IntegerField()
    article_author = models.CharField(max_length=30, default="QingLang")
    commit_date = models.DateField('dateCommit')

    class Meta:
        ordering = ['article_cate', '-commit_date']

    def __str__(self):
        return self.article_belongs() + "_" + self.acticle_title


    def article_belongs(self):
        cates = ["新闻中心","行业资讯","产品展示","产品和服务","活动主题","关于我们"]
        return cates[self.article_cate - 1]

class Top3p(models.Model):

    name = models.CharField(max_length=50) ##第几张图
    i = models.IntegerField()
    img = models.ImageField(upload_to='pic', default=".\media\pic\demo.png")

    def __str__(self):
        group = ['-','一', '二', '三']
        return '第' + group[self.i]+ "张图"

    class Meta:
        ordering = ['-i']
		
'''
class ImageStore(models.Model):
    name = models.CharField(max_length=150,null=True)
    img = models.ImageField(upload_to='img')


    class Meta:
        db_table = 'ImageStore'
'''



