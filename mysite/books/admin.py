# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:03:17 2015

@author: David
"""

from django.contrib import admin 
from books.models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Age', 'Country')

admin.site.register(Author) 
admin.site.register(Book)
