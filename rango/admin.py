from django.contrib import admin

from .models import Category, Page, UserProfile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', 'views', 'likes')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=('title', 'url', 'views', 'category')
    search_fields = ('title',)
    list_filter = ['category']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('user.username',)
