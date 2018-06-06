from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

# View function for the home page
def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()# Generate counts of some of the main objects
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()# Available books (status = 'a')
    num_authors=Author.objects.count() 
    
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    
    # Loads the Html template index.html with the data in it 
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,
            'num_visits':num_visits},
        ) # the request object (an HttpRequest), an HTML template, a context variable (a dictionary that has the data that will be put into the placeholders)

# View function for the book list page
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10 #Once it gets to ten it will go to the next page; /catalog/books/?page=2
    
# View function for the book detail page
class BookDetailView(generic.DetailView):
    model = Book
    

# View function for the book list page
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10 #Once it gets to ten it will go to the next page; /catalog/books/?page=2
    
# View function for the book detail page
class AuthorDetailView(generic.DetailView):
    model = Author
    
# View listing books on loan to current user
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    # Order by the due_back date so that the oldest items are displayed first
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')




# view listing all books on loan. Only visible to users with can_mark_returned permission.
class LoanedBooksAllListView(PermissionRequiredMixin,generic.ListView):
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name ='catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back') 


    