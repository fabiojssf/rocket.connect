from django.db import models
from instance.models import Server, Connector
import uuid


class LiveChatRoom(models.Model):

    class Meta:
        verbose_name = "Live Chat Room"
        verbose_name_plural = "Live Chat Rooms"

    def __str__(self):
        return self.token

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    connector = models.ForeignKey(Connector, on_delete=models.CASCADE, related_name="rooms")
    token = models.CharField(max_length=50)
    # meta
    created = models.DateTimeField(
        blank=True, auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(
        blank=True, auto_now=True, verbose_name="Updated")

class Message(models.Model):

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = 'created',

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    envelope_id = models.CharField(max_length=100)
    room = models.ForeignKey(LiveChatRoom, on_delete=models.CASCADE, related_name="messages", blank=True, null=True)
    connector = models.ForeignKey(Connector, on_delete=models.CASCADE, related_name="messages")
    raw_message = models.JSONField(blank=True, null=True)
    payload = models.JSONField(blank=True, null=True)
    response = models.JSONField(blank=True, null=True)
    delivered = models.BooleanField(null=True)
    # meta
    created = models.DateTimeField(
        blank=True, auto_now_add=True, verbose_name="Created"
    )
    updated = models.DateTimeField(
        blank=True, auto_now=True, verbose_name="Updated")
