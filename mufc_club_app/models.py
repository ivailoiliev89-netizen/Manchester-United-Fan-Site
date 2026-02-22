from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name='Player name')
    position = models.CharField(max_length=50, verbose_name='Position')
    number = models.PositiveBigIntegerField(verbose_name='Number')
    nationality = models.CharField(max_length=50, verbose_name='Nationality')
    image = models.ImageField(upload_to='players/',
                              default='players/default_avatar.png')

    def __str__(self):
        return f"{self.number}. {self.name}"

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'


class Coach(models.Model):
    name = models.CharField(max_length=100, verbose_name='Coach name')
    role = models.CharField(max_length=100, default='Head coach ')
    bio = models.TextField()
    image = models.ImageField(upload_to='coach/')
    wiki_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} is a {self.role}."


class FanMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Fan name')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = 'Fan message'
        verbose_name_plural = 'Fans messages'


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ClubInfo(models.Model):
    category = models.CharField(max_length=50, verbose_name='Category')
    details = models.TextField(verbose_name='Details')

    def __str__(self):
        return self.category


class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Title')
    image = models.ImageField(upload_to='gallery/', verbose_name='Image')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Picture {self.id}"

    class Meta:
        verbose_name = 'Picture at the gallery'
        verbose_name_plural = 'Gallery'
