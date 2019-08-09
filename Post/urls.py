from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views.bookmark import BookMarkViewSet
from .views.post import PostViewSet,search_tag
from .views.recentlyViewd import RecentlyViewdViewSet
from django.urls import path

router = DefaultRouter()


router.register('bookmark', BookMarkViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
router.register('post', PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
router.register('recentlyViewd', RecentlyViewdViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('tags/<tags>', search_tag),
# ]
