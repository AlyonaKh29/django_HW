from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, datetime
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all()
    context = {'books': books_list}
    return render(request, template, context)


def pub_date_view(request, pub_date='2021-01-02'):
    template = 'books/date_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    earlier = Book.objects.filter(pub_date__lt=pub_date)[-1]

    later = Book.objects.filter(pub_date__gt=pub_date)[0]

    context = {
        'books': books,
        'earlier': earlier,
        'later': later
    }
    return render(request, template, context)

