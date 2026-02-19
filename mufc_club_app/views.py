from django.shortcuts import render, redirect
from .models import Player, FanMessage, Coach
from .serializers import PlayerSerializer
from rest_framework import generics
from .forms import FanMessageForm


def home(request):
    coach = Coach.objects.first()
    return render(request, 'index.html', {'coach': coach})


def learn_more(request):
    return render(request, 'learn-more.html')


def players_list(request):
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
