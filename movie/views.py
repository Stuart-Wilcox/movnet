from django.shortcuts import loader, HttpResponse, HttpResponseRedirect
from general.models import Movie
from general.utils import auth


def movie_list(request):
    if not auth(request):
        return HttpResponseRedirect("/denied")

    template = loader.get_template('movie/movie_list.html')
    context = {
        'movies': Movie.objects.all(),
        'title': 'Movies'
    }
    return HttpResponse(template.render(context, request))


def movie_detail(request, index):
    if not auth(request):
        return HttpResponseRedirect("/denied")

    template = loader.get_template('movie/movie_detail.html')
    context = {
        'movie': Movie.objects.get(pk=index),
        'title': Movie.objects.get(pk=index).name,
    }
    return HttpResponse(template.render(context, request))
