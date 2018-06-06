from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # https://django-amra0760.c9users.io/catalog/
    
    path('books/', views.BookListView.as_view(), name='books'),# ListView is a class that inherits from an existing view #as_view since it will be implemented as a class
    # https://django-amra0760.c9users.io/catalog/books/
    
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    # https://django-amra0760.c9users.io/catalog/book/<id#>

    path('authors/', views.AuthorListView.as_view(), name='authors'),
    # https://django-amra0760.c9users.io/catalog/authors/
    
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # https://django-amra0760.c9users.io/catalog/authors/<id#>
    
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    # https://django-amra0760.c9users.io/catalog/mybooks/
    
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    # https://django-amra0760.c9users.io/catalog/borrowed/
    
]