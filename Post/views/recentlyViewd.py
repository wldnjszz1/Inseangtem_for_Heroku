from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..serializers.recentlyviewd import RecentlyViewdSerializer
from ..models.recentlyviewd import RecentlyViewd
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework import serializers
from ..models.post import Post
from Auth.models import IstUser
from django.core import serializers
from django.db.models import QuerySet


# TO DO : put 요청 시에 타임스탬프 시간 바꿔주기
class RecentlyViewdViewSet(viewsets.ModelViewSet):
    queryset = RecentlyViewd.objects.all()
    serializer_class = RecentlyViewdSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        recent_user_id = request.data.get("user_id")
        recent_post_id = request.data.get("post_id")

        print(recent_user_id)
        print(recent_post_id)

        post_id = Post.objects.get(pk=recent_post_id)
        user_id = IstUser.objects.get(pk=recent_user_id)

        count = RecentlyViewd.objects.count()

        compare = RecentlyViewd.objects.filter(post_id=post_id)

        if compare:
            compare.delete()
            RecentlyViewd.objects.create(user_id=user_id, post_id=post_id)
        else:
            if count < 5:
                RecentlyViewd.objects.create(user_id=user_id, post_id=post_id)
            else:
                earliest = RecentlyViewd.objects.earliest('lastTime')
                earliest.delete()
                RecentlyViewd.objects.create(user_id=user_id, post_id=post_id)
        # if count != 0:
        #     for i in getAll:
        #         print(i)
        #         if post_id == i.post_id:
        #             alreadyViewd = i.post_id
        #             alreadyViewd.delete()
        #             RecentlyViewd.objects.create(user_id=user_id, post_id=post_id)
        #         else:
        #             if count < 5:
        #                 RecentlyViewd.objects.create(user_id=user_id, post_id=post_id)
        #             else:
        #                 earliest = RecentlyViewd.objects.earliest('lastTime')
        #                 earliest.delete()
        #                 RecentlyViewd.objects.create(user_id=user_id, post_id=post_id)
        # else:
        #     RecentlyViewd.objects.create(user_id=user_id, post_id=post_id)

        serialized_obj = RecentlyViewd.objects.all()
        return HttpResponse(serialized_obj, content_type="application/json")
