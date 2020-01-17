from django.db import models  
  
  
class Author(models.Model):  
    full_name = models.TextField(max_length=100, unique=True, verbose_name='Имя')  
    birth_year = models.SmallIntegerField(verbose_name='Год рождения автора')  
    country = models.CharField(max_length=2, verbose_name='Страна автора')

    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Издательство')
    
    def __str__(self):
        return self.name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField(verbose_name='Название книги')  
    description = models.TextField(verbose_name='Описание')  
    year_release = models.SmallIntegerField(verbose_name='Год')  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    copy_count = models.IntegerField(default=1, verbose_name='Страна автора')
    price = models.DecimalField(max_digits = 10, decimal_places=2, default=0, verbose_name='Цена')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, verbose_name='Издательство')
