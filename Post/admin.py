from django.contrib import admin
from .models.recentlyviewd import RecentlyViewd
from .models.bookmark import BookMark
from .models.post import Post

# Register your models here.

admin.site.register(BookMark)
admin.site.register(Post)
admin.site.register(RecentlyViewd)
