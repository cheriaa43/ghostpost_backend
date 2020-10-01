from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ghostpost.serializers import BoastRoastSerializer
from ghostpost.models import Boast_Roast


# Create your views here.
class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = Boast_Roast.objects.all()
    serializer_class = BoastRoastSerializer
    
    
    # help from Nykal
    @action(detail=False)
    def boast(self, request):
        '''Shows boast post only'''
        boast = Boast_Roast.objects.filter(post_type=True).order_by('-date_created')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)
    
    
    @action(detail=False)
    def roast(self, request):
        '''Shows roast post only'''
        roast = Boast_Roast.objects.filter(post_type=False).order_by('-date_created')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['get','post'])
    def up_vote(self, request, pk=None):
        '''Adds a up vote to certian post'''
        post = self.get_object()
        post.up_vote += 1
        post.save()
        return Response({'status': 'upvoted'})
    
    
    @action(detail=True, methods=['get','post'])
    def down_vote(self, request, pk=None):
        '''Adds a down vote to certian post'''
        post = self.get_object()
        post.down_vote += 1
        post.save()
        return Response({'status': 'downvoted'})
