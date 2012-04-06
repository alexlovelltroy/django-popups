from django.db import models
from django.contrib.auth.models import User

class PopupRecord(models.model):
    user = models.ForeignKey(User)
    popup_name = models.CharField()
    first_seen = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'popup_name')
