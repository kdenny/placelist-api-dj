from django.db import models

class ArtistProfile(models.Model):
    name = models.CharField(max_length=150)
    artist_type = models.CharField(max_length=150, default='musician')
    genre = models.CharField(max_length=150, default='')
    city = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    soundcloud_id = models.CharField(max_length=25, default='')

        # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.name)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)

class Like(models.Model):
    artist_1 = models.ForeignKey(ArtistProfile, related_name='likes', on_delete=models.CASCADE)
    artist_2 = models.ForeignKey(ArtistProfile, related_name='liked_you', on_delete=models.CASCADE)
    swiped_on = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField(default=False)
    matched = models.BooleanField(default=False)

        # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.artist_1) + ' likes ' + str(self.liked_artist)

    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.artist_1) + ' likes ' + str(self.liked_artist)


class Message(models.Model):
    match = models.ForeignKey(Like, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(ArtistProfile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(ArtistProfile, related_name='received_messages', on_delete=models.CASCADE)
    message_text = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)


        # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.sender) + ' messaged ' + str(self.receiver)


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# Create your models here.
