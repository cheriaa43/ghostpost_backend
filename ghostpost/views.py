from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ghostpost.serializers import BoastRoastSerializer
from ghostpost.models import Boast_Roast
from rest_framework.parsers import JSONParser

# Create your views here.
class BoastRoastViewSet(viewsets.ModelViewSet):
    queryset = Boast_Roast.objects.all()
    serializer_class = BoastRoastSerializer
    
    
    def create(self, request):
        '''Create Post'''
        post_data = JSONParser().parse(request)
        
        print(post_data)
        # results = Boast_Roast.objects.create({
        #     content: request.data.content,
        #     post_type: request.data.post_type
        # })
        post = BoastRoastSerializer(data=post_data)
        if post.is_valid():
            post.save()
            return Response({'status': 'posted'})
        return Response({'status': 'invalid'})
        
    
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
    
    
    @action(detail=False)
    def highest_votes(self, request, pk=None):
        '''Highest total votes'''
        all_posts = Boast_Roast.objects.all()
        sorted_votes = list(all_posts)
        sorted_votes = sorted(sorted_votes, key=lambda a: a.num_votes, reverse=True)
        serializer = self.get_serializer(sorted_votes, many=True)
        return Response(serializer.data)
