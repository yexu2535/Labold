# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 22:59:29 2015

@author: David
"""

from django import forms
from django.forms import ModelForm
from books.models import Book, Author


class AddBookForm(ModelForm):
    class Meta:
        model = Book
    
class AddAuthorForm(ModelForm):
    class Meta:
        model = Author


        