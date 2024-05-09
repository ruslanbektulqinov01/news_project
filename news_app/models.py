from django.db import models

from account.models import CustomUser


class Artice(models.Model):
    WORLD = 'world'
    LOCAL = 'local'
    SPORT = 'sport'

    TAG = (
        (WORLD, 'world'),
        (LOCAL, 'local'),
        (SPORT, 'sport')
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, )
    image = models.ImageField(upload_to='image/')
    tag = models.CharField(max_length=10, choices=TAG, null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        return self.image.url

    def __str__(self):
        return f'{self.id}--{self.title}'


class Comment(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Artice, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Artice, on_delete=models.CASCADE)
    like = models.BooleanField(null=True, default=None)
    dislike = models.BooleanField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
