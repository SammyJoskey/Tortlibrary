from django.contrib import admin
from p_library.models import Book, Author, Publisher

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    @staticmethod
    def publisher_name(obj):
        return obj.publisher.name

    list_display = ('title', 'author', 'publisher', )
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publisher')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')
    fields = ('full_name', 'birth_year', 'country')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', )
