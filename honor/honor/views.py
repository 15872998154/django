from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Hero,HeroType
# Create your views here.
def index(request):
    context = {}

    #从数据库中取得所有的英雄
    all_heros = Hero.objects.all()

    context['all_heros'] = all_heros

    return render(request,'honor/index.html',context)

def gonglue(request,id):
    context = {}
    hero = get_object_or_404(Hero,hero_id = id)
    
    print(hero)
    context['hero'] = hero
    return render(request,'honor/gonglue.html',context)

def skill(request,id):
    context = {}
    hero = get_object_or_404(Hero,hero_id = id)
    
    print(hero)
    context['hero'] = hero
    return render(request,'honor/skill.html',context)