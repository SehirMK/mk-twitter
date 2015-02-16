from django.db import models



class Twit(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    content = models.TextField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    fav_count = models.IntegerField()
    rt_count = models.IntegerField()
    rt_users = models.ManyToManyField(User, related_name='rt_users')
    fav_users = models.ManyToManyField(User, related_name='fav_users')


    def __unicode__(self):
        return self.content