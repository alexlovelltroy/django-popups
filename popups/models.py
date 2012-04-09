from django.db import models
from django.contrib.auth.models import User

class PopupRecord(models.Model):
    user = models.ForeignKey(User)
    popup_name = models.CharField(max_length=255)
    first_seen = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('user', 'popup_name')
