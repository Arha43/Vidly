from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Movie
# Create your views here.

def index(requet):
    movies=Movie.objects.all()
    return render(requet,'index.html',{'movies':movies})
    #Select * from movies
    # Movie.objects.filter(release_year=1984)
    # Select * from movies where releaste date =1984


def detail(request,movie_id):
         movie=get_object_or_404(Movie,pk=movie_id)
    # try:
        #  movie= Movie.objects.get(pk=movie_id)
         return render(request,'detail.html',{'movie':movie})
    # except Movie.DoesNotExist:
    #    raise Http404()