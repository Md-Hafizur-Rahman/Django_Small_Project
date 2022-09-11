from re import A
from django.contrib import admin
# Register your models here.

from modelrelation.models import Like, Post, User, Page,Nasheed
from django.contrib import messages

admin.site.site_header = "PageAdminPanel"
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "password")
    # to remove add option:
    """ def active(self, obj):
        return obj.is_active == 1
    active.boolean = True
  
    def has_add_permission(self, request):
        return False """
    
def change_rating(modeladmin, request, queryset):
    queryset.update(favourite = 'True')
    messages.success(request, "Selected Record(s) Marked as favourite Successfully !!")
# Action description
change_rating.short_description = "Mark Selected page as favourite"

def make_inactive(modeladmin, request, queryset):
        queryset.update(favourite = 'False')
        messages.success(request, "Selected Record(s) Marked as Unfavourite Successfully !!")
# Action description
make_inactive.short_description = "Mark Selected page as Unfavourite"
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("user","page_name","page_cat","page_publish_date")
    actions = [change_rating,make_inactive]  
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("connect","page_name","page_cat","page_publish_date","count")

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id","user","post_title","post_cat","post_publish_date")
@admin.register(Nasheed)
class NasheedAdmin(admin.ModelAdmin):
    list_display = ("nasheed_name","nasheed_duration","writen_by")
