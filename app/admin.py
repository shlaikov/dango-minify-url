from django.contrib import admin

from .models import ShortUrl, Hit


class ShortUrlAdmin(admin.ModelAdmin):
    fields = ('target', 'key')
    list_display = ('key', 'target', 'added')
    ordering = ('-added',)
    list_filter = ('added',)
    date_hierarchy = 'added'

admin.site.register(ShortUrl, ShortUrlAdmin)


class HitAdmin(admin.ModelAdmin):
    list_display = ('target', 'ip', 'user_agent', 'referer', 'time')
    ordering = ('-time',)
    list_filter = ('target', 'referer', 'time')
    date_hierarchy = 'time'

admin.site.register(Hit, HitAdmin)