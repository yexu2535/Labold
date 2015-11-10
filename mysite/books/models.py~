# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length=50, verbose_name=u"姓名")
    Age = models.IntegerField(verbose_name=u"年龄")
    Country = models.CharField(max_length=20, verbose_name=u"国籍")
    
    def __unicode__(self):
        return self.Name

class Book(models.Model):
    ISBN = models.CharField(max_length=30, primary_key=True, verbose_name=u"书号")
    title = models.CharField(max_length=100, verbose_name=u"书名")
    authors = models.ManyToManyField(Author, verbose_name=u"作者")
    Publisher = models.CharField(max_length=30, verbose_name=u"出版商")
    PublishDate = models.DateField(verbose_name=u"出版日期")
    price = models.FloatField(verbose_name=u"价格")
    
    def __unicode__(self):
        return self.ISBN