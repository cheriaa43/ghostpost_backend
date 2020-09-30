from rest_framework import serializers
from ghostpost.models import Boast_Roast

class BoastRoastSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Boast_Roast
        fields = ['id', 'post_type', 'up_vote', 'down_vote', 'content', 'date_created', 'num_votes']
