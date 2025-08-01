from django.db import models

class Set(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True, max_length=500)
    image = models.ImageField(upload_to='posters/', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
class Film (models.Model):
    set = models.ForeignKey(Set, related_name='films', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='posters/', blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    ### РЕАЛИЗОВАТЬ ЖАНРЫ И РЕЖИССЁРОВ
    
    

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['release_date']
        
    def __str__(self):
        return self.title

