from django.db import models
from django.utils import timezone

# Create your models here.
class Boast_Roast(models.Model):
    Post_Choice = ((True, 'Boast'), (False, 'Roast'))
    post_type = models.BooleanField(choices=Post_Choice)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    content = models.CharField(max_length=280)
    date_created = models.DateTimeField(default=timezone.now)

    @property
    def num_votes(self):
        return self.up_vote + self.down_vote