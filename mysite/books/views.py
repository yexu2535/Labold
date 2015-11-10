# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from books.models import Book, Author
from books.forms import AddBookForm, AddAuthorForm
   
#def search_form(request):    
#    return render_to_response('search_form.html')

def search(request):   
    error = False
    if 'q' in request.POST:       
        q = request.POST['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(authors__Name__icontains=q)
            return render_to_response('search_result.html',
                {'books': books, 'query': q})
    return render_to_response('home.html', {'error': error})
    
def details(request):
    if 'q' in request.GET:
        q = request.GET['q']
        book = Book.objects.get(ISBN=q)
        author_t = book.authors.all()
        return render_to_response('display.html',
                {'book': book, 'author_t': author_t})

def display(request):
    books = Book.objects.all()
    return render_to_response('home.html',
                {'books': books})
                
def delete(request):
    if 'q' in request.GET:
        q = request.GET['q']
        book = Book.objects.filter(ISBN=q)
        book.delete()
        return render_to_response('delete.html')
        
def add_book(request):
    book = None    
    error = False
    if request.POST:
        temp = Book()        
        book = AddBookForm(request.POST, instance = temp)
        if book.is_valid():
            book.save()
            return HttpResponseRedirect('/add/success/')
        else:
            error = True
            book = AddBookForm()
            return render_to_response('add_book.html',
                    {'book': book, 'error': error})
    book = AddBookForm()
    return render_to_response('add_book.html',
                    {'book': book, 'error': error})
                    
def add_author(request):
    author = None
    error = False
    if request.POST:
        temp = Author()
        author = AddAuthorForm(request.POST, instance = temp)
        if author.is_valid():
            author.save()
            return HttpResponseRedirect('/add/success/')
        else:
            error = True
            author = AddAuthorForm()
            return render_to_response('add_author.html',
                    {'author': author, 'error': error})
    author = AddAuthorForm()
    return render_to_response('add_author.html',
                    {'author': author, 'error': error})

def success(request):
    return render_to_response('success.html')
        
        
def update(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        temp = Book.objects.get(ISBN=q)
        if request.POST:
            book = AddBookForm(request.POST, instance = temp)
            if book.is_valid():
                book.save()
                return HttpResponseRedirect('/update/success/')
            else:
                error = True
                book = AddBookForm(instance = temp)
                return render_to_response('update.html',
                        {'book': book, 'error': error})
    book = AddBookForm(instance = temp)
    return render_to_response('update.html',
                    {'book': book, 'error': error})
        
def update_success(request):
    return render_to_response('update_success.html')