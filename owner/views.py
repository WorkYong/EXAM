import json

from django.http import JsonResponse
from django.views import View

from owner.models import Owner, Dog

class OwnerView(View): # 주인의 정보를 쉽게 넣어본다
    def post(self, request):
        data = json.loads(request.body)
        
        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )       
       
        return JsonResponse({'messasge':'created'}, status=201)
        
    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dog_list = []
            dog_infos = owner.dog_set.all()
            for dog_info in dog_infos:
                dog_list.append(
                    {
                        "dog_name" : dog_info.name,
                        "dog_age" : dog_info.age,
                    }
                )

            results.append(
                {
                    "owner_name" : owner.name, 
                    "email" : owner.email,
                    "owner_age" : owner.age,
                    "dog_information" : dog_list, 
                }
            )

        return JsonResponse({'results':results}, status=200)    

class DogView(View) :
    def post(self, request):
        data = json.loads(request.body)

        Dog.objects.create(
            name = data['dog_name'],
            age = data['dog_age'],
            owner = Owner.objects.get(name=data['owner']),

        )

        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    "dog_name" : dog.name,
                    "owner" : dog.owner.name, 
                    "dog_age" : dog.age
                }
            )
        return JsonResponse({'resutls':results}, status=200)      
