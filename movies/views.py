from django.views import generic
from .models import Movie
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SearchForm


# List view displays a list of objects (i.e. Movies)
class IndexView(generic.ListView):
    # List view needs a context to be provided explicitly, otherwise a
    context_object_name = 'latest_movies'
    template_name = 'movies/index.html'

    def get_queryset(self):
        return Movie.objects.order_by('title')


# Detail view displays a details of a Movie object
class DetailView(generic.DeleteView):
    # For DetailView the question variable is provided automatically – since we’re using a Django model(Question),
    # Django is able to determine an appropriate name for the context variable.
    # Also the DetailView generic view expects the primary key value captured from the URL to be called "pk",
    # so we’ve changed question_id to pk for the generic views in polls/urls.py
    model = Movie
    template_name = 'movies/detail.html'


abc = 'THIS IS SOME SHIT GOING ON!'


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'movies/movie.html', {'form': form})
