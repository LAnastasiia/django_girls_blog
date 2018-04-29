from django.contrib import admin
from comment.models import Comment, Reaction

admin.site.register(Comment)
admin.site.register(Reaction)
