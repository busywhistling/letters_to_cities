from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import City, Letter
from .forms import LetterForm

# Create your views here.
class CityListView(generic.ListView):
    template_name = "cities/city_list.html"
    context_object_name = "cities_list"

    def get_queryset(self):
        """Return the list of all cities"""
        return City.objects.all()

class CityDetailView(generic.DetailView):
    model = City
    template_name = "cities/city_detail.html"
    context_object_name = "city"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['letters'] = context['city'].letter_set.all()
        return context

def write_letter(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = LetterForm(request.POST)
        # check whether it's valid
        if form.is_valid():
            Letter(city=city, content=form.cleaned_data["letter"], author=form.cleaned_data["author"]).save()
            return HttpResponseRedirect(f'/{pk}')
    else:
        form = LetterForm()
        return render(request, "cities/write_letter.html", {"city": city, "form": form})


def page_not_found(request, exception):
    return render(request, "cities/404.html")