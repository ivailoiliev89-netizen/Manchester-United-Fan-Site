from django.contrib import admin
from .models import Player, FanMessage, Coach, News, ClubInfo, GalleryImage

admin.site.register(Player)
admin.site.register(FanMessage)
admin.site.register(Coach)
admin.site.register(News)
admin.site.register(ClubInfo)
admin.site.register(GalleryImage)
