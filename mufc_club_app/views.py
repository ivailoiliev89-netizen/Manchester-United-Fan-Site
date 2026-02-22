from django.shortcuts import render, redirect
from .models import Player, FanMessage, Coach, News, ClubInfo, GalleryImage
from .serializers import PlayerSerializer
from rest_framework import generics
from .forms import FanMessageForm
from django.db.models import Q


def home(request):
    coach = Coach.objects.first()
    news_list = News.objects.all().order_by('-created_at')[:1]
    info_list = ClubInfo.objects.all()[:3]
    gallery_photos = GalleryImage.objects.all().order_by('-uploaded_at')

    context = {
        'coach': coach,
        'news_list': news_list,
        'info_list': info_list,
        'gallery_photos': gallery_photos
    }

    return render(request, 'index.html', context)


def learn_more(request):
    return render(request, 'learn-more.html')


def players_list(request):
    query = request.GET.get('q')
    if query:
        players = Player.objects.filter(Q
                                        (name__icontains=query) | Q(position__icontains=query))
    else:
        players = Player.objects.all().order_by('number')
    return render(request, 'players.html', {'players': players})


def fan_zone(request):
    if request.method == 'POST':
        form = FanMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('club:fan_zone')
    else:
        form = FanMessageForm()
    messages = FanMessage.objects.all().order_by('-created_at')
    return render(request, 'fan_zone.html', {'form': form, 'messages': messages})


class PlayerListAPI(generics.ListAPIView):
    queryset = Player.objects.all().order_by('number')
    serializer_class = PlayerSerializer
