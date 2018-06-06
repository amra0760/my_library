from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

# Adds the Book information inline to the Author
# class BookInline(admin.TabularInline):
#     model = Book

# Register the Admin classes for Author using the decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    # inlines = [BookInline]
# admin.site.register(Author, AuthorAdmin)


# Adds the BookInstance information inline to the Book details
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre','language')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status','borrower', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )