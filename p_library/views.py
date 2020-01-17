from django.http import HttpResponse
from django.template import loader
from .models import Book, Author, Publisher
from django.shortcuts import redirect


def home(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def book_list(request):
    template = loader.get_template('book_list.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


def author_list(request):
    template = loader.get_template('author_list.html')
    author = Author.objects.all()
    biblio_data = {
        "objects_list": author,
    }
    return HttpResponse(template.render(biblio_data, request))

def publisher_list(request):
    template = loader.get_template('publisher_list.html')
    publisher = Publisher.objects.all().order_by('name')

    biblio_data = {
        "objects_list": publisher,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            book.copy_count += 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')
