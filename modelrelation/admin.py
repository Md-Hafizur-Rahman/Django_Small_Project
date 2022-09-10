from re import A
from django.contrib import admin

# Register your models here.

from modelrelation.models import User, Page
from django.contrib import messages



admin.site.site_header = "PageAdminPanel"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "password")
    
    # to remove add option:
    def active(self, obj):
        return obj.is_active == 1
    active.boolean = True
  
    def has_add_permission(self, request):
        return False
    
def change_rating(modeladmin, request, queryset):
    queryset.update(favourite = 'True')
    messages.success(request, "Selected Record(s) Marked as favourite Successfully !!")

# Action description
change_rating.short_description = "Mark Selected page as favourite"
def make_inactive(modeladmin, request, queryset):
        queryset.update(favourite = 'False')
        messages.success(request, "Selected Record(s) Marked as Unfavourite Successfully !!")
make_inactive.short_description = "Mark Selected page as Unfavourite"

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("user","page_name","page_cat","page_publish_date")
    actions = [change_rating,make_inactive]  
    
    