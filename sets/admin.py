from django.contrib import admin
from .models import Set, Film
# Register your models here.
@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'slug')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'release_date', 'set', 'image', 'slug')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('release_date', 'set')
    list_editable = ('description', 'set', 'image',)