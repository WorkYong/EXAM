import json
from django.http     import JsonResponse

from django.views import View

from movie.models import Actor, Movie, Bridge

class ActorView(View): # 주인의 정보를 쉽게 넣어본다
    def post(self, request):
        data = json.loads(request.body)
        
        Actor.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            birth = data['birth']
        )       
       
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):					
        actors = Actor.objects.all()
        results =[]
        for actor in actors:
            actor_info = {
                'name' : actor.first_name + "  " + actor.last_name,
                'birth' : actor.birth
            }
            results.append(actor_info)				
            movies = actor.movie_set.all()	
            results2 =[]
            for movie in movies: 			 
                results2.append(movie.title)		
            results.append(results2)			
        return JsonResponse({'results':results}, status=200)


class MovieView(View):
    def post(self, request):					
        data = json.loads(request.body)
        movie = Movie.objects.create(
            title = data['title'],
            release = data['release_date'],
            running_time = data['running_time']
        )

        return JsonResponse({'MASSAGE':'SUCCESS'}, status=201)    

    def get(self, request):					# http GET 127.0.0.1:8000/actors/movies/
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            movie_info = {
                'movie_name' : movie.title,
                'release_date' : movie.release
            }
            results.append(movie_info)
            actors = movie.actor.all()				
            results2=[]
            for actor in actors:
                actor_info = {
                    'cast' : actor.first_name + actor.last_name
                }
                results2.append(actor_info)			
            results.append(results2)				

        return JsonResponse({'results':results}, status=200)


class BridgeView(View):
    def post(self, request):
        data  = json.loads(request.body)
        actor = Actor.objects.get(first_name=data['first_name'])
        movie = Movie.objects.get(title=data['title'])
        bridge = Bridge.objects.create(
            actor = actor,
            movie = movie
        )

        return JsonResponse({'MASSAGE':'SUCCESS'}, status=201)             