from django.db import models
from django.utils import timezone

class Comment(models.Model):
    """
    Class for comments (can't be moderated).
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post =  models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.content[:15] + '...'

    def __repr__(self):
        return self.author.username + self.content[:15] + '...'


class Reaction(models.Model):
    """
    Class for reactions on comment (bool value) to count users' likes
    and dislikes.
    """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment =  models.ForeignKey('comment.Comment', on_delete=models.CASCADE)
    agree = models.BooleanField()

    def __str__(self):
        r = 'agree' if self.agree else 'no'
        return r
